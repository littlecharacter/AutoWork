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
                time.sleep(1)
        except:
            pass


@unique
class OperateTypeEnum(Enum):
    LEFT_CLICK = {'code': 1, 'desc': '单击'}
    DOUBLE_CLICK = {'code': 2, 'desc': '双击'}
    RIGHT_CLICK = {'code': 3, 'desc': '右击'}
    LEFT_CLICK_IMG = {'code': 4, 'desc': '单击图片'}
    DOUBLE_CLICK_IMG = {'code': 5, 'desc': '双击图片'}
    KEY_PRESS = {'code': 6, 'desc': '按键'}
    HOT_KEY = {'code': 7, 'desc': '热键'}
    KEY_MAP = {'code': 8, 'desc': '快捷键'}
    INPUT = {'code': 9, 'desc': '输入'}
    OPEN_APP = {'code': 10, 'desc': '打开APP'}

    @staticmethod
    def get_enum(code):
        for e in OperateTypeEnum:
            if code == e.value['code']:
                return e

    def code(self):
        return self.value['code']

    def desc(self):
        return self.value['desc']


def execute(self, op_type, op_content):
    print(op_content)
    op_type_enum = OperateTypeEnum.get_enum(op_type)
    # 1-单击
    if op_type_enum == OperateTypeEnum.LEFT_CLICK:
        position = op_content.split(",")
        x, y = pyautogui.position()
        pyautogui.moveTo(x=x+int(position[0]), y=y+int(position[1]), duration=0.25)
        pyautogui.click()
        return True
    # 2-双击
    elif op_type_enum == OperateTypeEnum.DOUBLE_CLICK:
        position = op_content.split(",")
        x, y = pyautogui.position()
        pyautogui.moveTo(x=x + int(position[0]), y=y + int(position[1]), duration=0.25)
        pyautogui.doubleClick()
        return True
    # 3-右击
    elif op_type_enum == OperateTypeEnum.RIGHT_CLICK:
        position = op_content.split(",")
        x, y = pyautogui.position()
        pyautogui.moveTo(x=x + int(position[0]), y=y + int(position[1]), duration=0.25)
        pyautogui.rightClick()
        return True
    # 4-单击图片
    elif op_type_enum == OperateTypeEnum.LEFT_CLICK_IMG:
        return click_img(self.wid, op_content, 1)
    # 5-单击图片
    elif op_type_enum == OperateTypeEnum.DOUBLE_CLICK_IMG:
        return click_img(self.wid, op_content, 2)
    # 6-按键
    elif op_type_enum == OperateTypeEnum.KEY_PRESS:
        pyautogui.press(op_content)
        return True
    # 7-热键
    elif op_type_enum == OperateTypeEnum.HOT_KEY:
        keys = op_content.split(",")
        pyautogui.hotkey(keys[0], keys[1])
        return True
    # 8-快捷键
    elif op_type_enum == OperateTypeEnum.KEY_MAP:
        keys = op_content.split("+")
        for key in keys[0:-1]:
            pyautogui.keyDown(key)
        pyautogui.press(keys[-1])
        keys.reverse()
        for key in keys[1:]:
            pyautogui.keyUp(key)
        return True
    # 9-输入
    elif op_type_enum == OperateTypeEnum.INPUT:
        pyperclip.copy(op_content)
        time.sleep(0.5)
        if platform.system().lower() == 'windows':
            pyautogui.hotkey('ctrl', 'v')
        else:
            pyautogui.hotkey('command', 'v')
        return True
    # 10-打开APP
    elif op_type_enum == OperateTypeEnum.OPEN_APP:
        if platform.system().lower() == 'windows':
            subprocess.Popen(op_content)
        else:
            os.system(f'open \"{op_content}\"')
        return True
    return False


def click_img(wid, op_content, click_num):
    # 屏幕缩放系数 mac缩放是2 windows一般是1
    screenScale = pyautogui.screenshot().size[0] / pyautogui.size()[0]
    # print(pyautogui.size())
    # print(f"屏幕缩放系数：{screenScale}")

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
    if maxVal >= 0.8:
        # 计算出中心点(因为截图就是原图，所以这里要缩放)
        tagHalfW = int(targetWidth / screenScale / 2)
        tagHalfH = int(targetHeight / screenScale / 2)
        tagCenterX = maxLoc[0] / screenScale + tagHalfW
        tagCenterY = maxLoc[1] / screenScale + tagHalfH
        # 左键点击屏幕上的这个位置
        print(f"tagCenterX:{tagCenterX},tagCenterY:{tagCenterY}")
        # pyautogui.click(tagCenterX, tagCenterY, button='left')
        pyautogui.moveTo(x=tagCenterX, y=tagCenterY, duration=0.25)
        if click_num == 1:
            pyautogui.click()
        elif click_num == 2:
            pyautogui.doubleClick()
        return True
    print(f"没有匹配到{op_content}")
    return False
