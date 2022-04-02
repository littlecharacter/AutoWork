import json

DB_PATH = './db/auto_work.db'

WORK_FILENAME = './db/work_item.json'
FLOW_FILENAME = './db/work_flow.json'
MONITOR_FILENAME = './db/work_monitor.json'


def get_all_data(filename):
    with open(filename, encoding="utf-8") as f:
        data = json.load(f, encoding="utf-8")
    return data


def get_special_data(wid, filename):
    with open(filename, encoding="utf-8") as f:
        data = json.load(f, encoding="utf-8")
    for d in data:
        if d.get('wid') == int(wid):
            return d
    return None


class WorkItem:
    def __init__(self, wid, name):
        self.wid = wid
        self.name = name


class WorkFlow:
    def __init__(self, fid, name, order):
        self.fid = fid
        self.name = name
        self.order = order


class WorkMonitor:
    def __init__(self, mid, name):
        self.mid = mid
        self.name = name


class WorkOperate:
    def __init__(self, op_type, op_content, order):
        self.op_type = op_type
        self.op_content = op_content
        self.order = order
