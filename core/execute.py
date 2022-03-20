import os
import time
import copy
import threading
from enum import Enum, unique
from queue import Queue
from core.orm import *
import cv2
import pyautogui
import pyperclip
import pyscreeze
import subprocess
import platform

import random

pyautogui.FAILSAFE = False

run_flag = Queue(1)
run_work = {}
stop_signal = Queue(1)


class WorkThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.wid = None

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        try:
            run_flag.put_nowait(self)
            global run_work
            run_work['wid'] = self.wid
            flow_dict = get_special_data(self.wid, FLOW_FILENAME)
            flow_dict['flow'] = sorted(flow_dict['flow'], key=lambda x: x['order'])
            flow_item_list = copy.deepcopy(flow_dict['flow'])
            monitor_item_list = []
            monitor_dict = get_special_data(self.wid, MONITOR_FILENAME)
            if monitor_dict:
                monitor_item_list = monitor_dict['monitor']
            while True:
                if stop_signal.full():
                    break
                # 执行流程
                if not flow_item_list:
                    flow_item_list = copy.deepcopy(flow_dict['flow'])
                flow_item = flow_item_list[0]
                if execute(self, flow_item['op_type'], flow_item['op_content']):
                    flow_item_list.remove(flow_item)
                # 执行监控
                if monitor_item_list:
                    for monitor_item in monitor_item_list:
                        execute(self, monitor_item['op_type'], monitor_item['op_content'])
                time.sleep(3)
        except:
            pass


@unique
class OperateTypeEnum(Enum):
    LEFT_CLICK = 1
    RIGHT_CLICK = 2
    DOUBLE_CLICK = 3
    KEY_PRESS = 4
    DOUBLE_KEY_PRESS = 5
    INPUT = 6
    OPEN_APP = 7
    LOCATE_IMG = 8
    KEY_MAP = 9
    SCHEDULE = 10


def execute(self, op_type, op_content):
    if op_type == OperateTypeEnum.LEFT_CLICK.value:
        position = op_content.split(",")
        x, y = pyautogui.position()
        pyautogui.moveTo(x=x+int(position[0]), y=y+int(position[1]), duration=0.25)
        pyautogui.click()
        return True
    elif op_type == OperateTypeEnum.RIGHT_CLICK.value:
        position = op_content.split(",")
        x, y = pyautogui.position()
        pyautogui.moveTo(x=x + int(position[0]), y=y + int(position[1]), duration=0.25)
        pyautogui.rightClick()
        return True
    elif op_type == OperateTypeEnum.DOUBLE_CLICK.value:
        position = op_content.split(",")
        x, y = pyautogui.position()
        pyautogui.moveTo(x=x + int(position[0]), y=y + int(position[1]), duration=0.25)
        pyautogui.doubleClick()
        return True
    elif op_type == OperateTypeEnum.KEY_PRESS.value:
        pyautogui.press(op_content)
        return True
    elif op_type == OperateTypeEnum.DOUBLE_KEY_PRESS.value:
        keys = op_content.split(",")
        pyautogui.hotkey(keys[0], keys[1])
        return True
    elif op_type == OperateTypeEnum.INPUT.value:
        pyperclip.copy(op_content)
        time.sleep(0.5)
        if platform.system().lower() == 'windows':
            pyautogui.hotkey('ctrl', 'v')
        else:
            pyautogui.hotkey('command', 'v')
        return True
    elif op_type == OperateTypeEnum.OPEN_APP.value:
        if platform.system().lower() == 'windows':
            subprocess.Popen(op_content)
        else:
            os.system(f'open \"{op_content}\"')
        return True
    elif op_type == OperateTypeEnum.LOCATE_IMG.value:
        locate_img(self.wid, op_content)
        return True
    elif op_type == OperateTypeEnum.KEY_MAP.value:
        keys = op_content.split("+")
        for key in keys[0:-1]:
            pyautogui.keyDown(key)
        pyautogui.press(keys[-1])
        keys.reverse()
        for key in keys[1:]:
            pyautogui.keyUp(key)
        return True
    elif op_type == OperateTypeEnum.SCHEDULE.value:
        time.sleep(int(op_content))
        return True
    return False


def locate_img(wid, op_content):
    # 屏幕缩放系数 mac缩放是2 windows一般是1
    screenScale = pyautogui.screenshot().size[0] / pyautogui.size()[0]
    # print(pyautogui.size())
    print(f"屏幕缩放系数：{screenScale}")

    # 事先读取按钮截图
    img_path = f"./img/{wid}/{op_content}"
    target = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    targetHeight, targetWidth = target.shape[:2]

    # 先截图
    screenshot = pyscreeze.screenshot('./img/screenshot.png')
    # 读取图片 灰色会快
    source = cv2.imread(r'./img/screenshot.png', cv2.IMREAD_GRAYSCALE)
    # sourceHeight, sourceWidth = source.shape[:2]
    # 先缩放屏幕截图(本程序中无需缩放，因为截图就是原图)
    # sourceScale = cv2.resize(source, (int(sourceWidth / screenScale), int(sourceHeight / screenScale)), interpolation=cv2.INTER_AREA)
    # print(sourceScale.shape[:2])

    # 匹配图片
    matchResult = cv2.matchTemplate(source, target, cv2.TM_CCOEFF_NORMED)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(matchResult)
    # print(f"minVal:{minVal},maxVal:{maxVal},minLoc:{minLoc},maxLoc:{maxLoc}")
    if maxVal >= 0.9:
        # 计算出中心点(因为截图就是原图，所以这里要缩放)
        tagHalfW = int(targetWidth / screenScale / 2)
        tagHalfH = int(targetHeight / screenScale / 2)
        tagCenterX = maxLoc[0] / screenScale + tagHalfW
        tagCenterY = maxLoc[1] / screenScale + tagHalfH
        # 左键点击屏幕上的这个位置
        print(f"tagCenterX:{tagCenterX},tagCenterY:{tagCenterY}")
        pyautogui.click(tagCenterX, tagCenterY, button='left')
