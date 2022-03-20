import json


WORK_FILENAME = './db/work_item.json'
FLOW_FILENAME = './db/work_flow.json'
MONITOR_FILENAME = './db/work_monitor.json'


def get_all_data(filename):
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_special_data(wid, filename):
    with open(filename, encoding="utf-8") as f:
        data = json.load(f)
    for d in data:
        if d.get('wid') == int(wid):
            return d
    return None


class Work:
    def __init__(self, wid, name):
        self.wid = wid
        self.name = name
        self.flow: WorkFlow
        self.monitor: WorkMonitor


class WorkFlow:
    def __init__(self, fid, name, order):
        self.fid = fid
        self.name = name
        self.order = order
        self.operate: Operate


class WorkMonitor:
    def __init__(self, mid, name):
        self.mid = mid
        self.name = name
        self.operate: Operate


class Operate:
    def __init__(self, op_type, op_content, order):
        self.op_type = op_type
        self.op_content = op_content
        self.order = order
