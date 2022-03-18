import os
import time
import threading
from enum import Enum, unique
from queue import Queue
from core.orm import *

run_status = Queue(1)


run_work = {}
run_flow = {}
run_monitor = {}


class WorkThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.wid = None

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        run_status.put_nowait(1)
        print(os.getcwd())
        flow_dict = get_special_data(self.wid, FLOW_FILENAME)
        monitor_dict = get_special_data(self.wid, MONITOR_FILENAME)
        while True:
            if flow_dict:
                print(flow_dict)
            if monitor_dict:
                print(monitor_dict)
            print(self.wid)
            time.sleep(3)


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


def execute(op_type):
    if op_type == OperateTypeEnum.LEFT_CLICK.value:
        pass
    elif op_type == OperateTypeEnum.RIGHT_CLICK.value:
        pass
