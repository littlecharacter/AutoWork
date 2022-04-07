import json
from peewee import *
import datetime

DB_PATH = './db/auto_work.db'

WORK_FILENAME = './db/work_item.json'
FLOW_FILENAME = './db/work_flow.json'
MONITOR_FILENAME = './db/work_monitor.json'

# 数据库文件的路径和文件名称
db = SqliteDatabase(DB_PATH)


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


class BaseModel(Model):
    class Meta:
        database = db


class WorkItem(BaseModel):
    name = CharField()
    create_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'work_item'


class WorkFlow(BaseModel):
    wid = BigIntegerField()
    name = CharField()
    order = IntegerField()
    create_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'work_flow'
        indexes = (
            (('wid', 'order'), True),
        )


class WorkFlowBO:
    work_flow = None
    work_operate = []


class WorkMonitor(BaseModel):
    wid = BigIntegerField()
    name = CharField()
    create_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'work_monitor'


class WorkMonitorBO:
    work_monitor = None
    work_operate = []


class WorkOperate(BaseModel):
    fmid = BigIntegerField()
    op_type = IntegerField()
    op_content = CharField()
    order = IntegerField()
    create_at = DateTimeField(default=datetime.datetime.now())

    class Meta:
        db_table = 'work_operate'
        indexes = (
            (('fmid', 'order'), True),
        )
