import threading
import time
from enum import Enum, unique
import json
import os


FLOW_FILENAME = './db/work_flow.json'
MONITOR_FILENAME = './db/work_monitor.json'


def get_data(wid, filename):
    with open(filename) as f:
        data = json.load(f)
    for d in data:
        if d.get('wid') == wid:
            return d
    return None


class WorkThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.wid = None

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        print(os.getcwd())
        flow_dict = get_data(self.wid, FLOW_FILENAME)
        monitor_dict = get_data(self.wid, MONITOR_FILENAME)
        while True:
            if flow_dict:
                print(flow_dict)
            if monitor_dict:
                print(monitor_dict)
            print(self.wid)
            time.sleep(3)


class Work:
    def __init__(self, wid, flow, monitor):
        self.wid = wid
        self.flow: WorkFlow = flow
        self.monitor: WorkMonitor = monitor


class WorkFlow:
    def __init__(self, fid, suffix, operate):
        self.fid = fid
        self.suffix = suffix
        self.operate: Operate = operate


class WorkMonitor:
    def __init__(self, mid, suffix, operate):
        self.mid = mid
        self.suffix = suffix
        self.operate = operate


class Operate:
    def __init__(self, op_type, op_content, order):
        self.op_type = op_type
        self.op_content = op_content
        self.order = order


@unique
class OperateTypeEnum(Enum):
    LEFT_CLICK = 1
    RIGHT_CLICK = 2
    DOUBLE_CLICK = 3
    KEY_PRESS = 4
    DOUBLE_KEY_PRESS = 5
    INPUT = 6


def execute(op_type):
    if op_type == OperateTypeEnum.LEFT_CLICK.value:
        pass
    elif op_type == OperateTypeEnum.RIGHT_CLICK.value:
        pass
