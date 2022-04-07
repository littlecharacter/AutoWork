import json
from peewee import *
import datetime
from enum import Enum, unique

DB_PATH = './db/auto_work.db'

FLOW_FILENAME = './db/work_flow.json'
MONITOR_FILENAME = './db/work_monitor.json'

# 数据库文件的路径和文件名称
db = SqliteDatabase(DB_PATH)


# 操作工作项
def insert_work_item(work_item):
    WorkItem.create_table()
    work_item.save()


def update_work_item(work_item):
    WorkItem.create_table()
    work_item.save()


def delete_work_item(work_item):
    WorkItem.create_table()
    work_item.delete_instance()


def select_work_items():
    WorkItem.create_table()
    return list(WorkItem.select().order_by(WorkItem.id.asc()))


# 操作工作流程
def insert_work_flow(work_flow):
    WorkFlow.create_table()
    work_flow.save()


def update_work_flow(work_flow):
    WorkFlow.create_table()
    work_flow.save()


def delete_work_flow(work_flow):
    WorkFlow.create_table()
    work_flow.delete_instance()


def select_work_flows(wid):
    WorkFlow.create_table()
    work_flows = list(WorkFlow.select().where(WorkFlow.wid == wid).order_by(WorkFlow.order.asc()))
    work_flow_bos = []
    for work_flow in work_flows:
        work_flow_bo = WorkFlowBO()
        work_flow_bo.work_flow = work_flow
        work_operates = select_work_operates(work_flow.id, FMTypeEnum.FLOW.value)
        work_flow_bo.work_operates = work_operates
        work_flow_bos.append(work_flow_bo)
    return work_flow_bos


# 操作工作监控
def insert_work_monitor(work_monitor):
    WorkMonitor.create_table()
    work_monitor.save()


def update_work_monitor(work_monitor):
    WorkMonitor.create_table()
    work_monitor.save()


def delete_work_monitor(work_monitor):
    WorkMonitor.create_table()
    work_monitor.delete_instance()


def select_work_monitors(wid):
    WorkMonitor.create_table()
    work_monitors = list(WorkMonitor.select().where(WorkMonitor.wid == wid))
    work_monitor_bos = []
    for work_monitor in work_monitors:
        work_monitor_bo = WorkMonitorBO()
        work_monitor_bo.work_monitor = work_monitor
        work_operates = select_work_operates(work_monitor.id, FMTypeEnum.MONITOR.value)
        work_monitor_bo.work_operates = work_operates
        work_monitor_bos.append(work_monitor_bo)
    return work_monitor_bos


# 操作工作操作
def insert_work_operate(work_operate):
    WorkOperate.create_table()
    work_operate.save()


def update_work_operate(work_operate):
    WorkOperate.create_table()
    work_operate.save()


def delete_work_operate(work_operate):
    WorkOperate.create_table()
    work_operate.delete_instance()


def select_work_operates(fm_id, fm_type):
    WorkOperate.create_table()
    return list(WorkOperate.select().where((WorkOperate.fm_id == fm_id) & (WorkOperate.fm_type == fm_type)).order_by(WorkOperate.order.asc()))


# 一开始的写法
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
    create_at = DateTimeField(
        constraints=[SQL("DEFAULT (datetime('now'))")],
        default=datetime.datetime.now().replace(microsecond=0)
    )

    class Meta:
        db_table = 'work_item'


class WorkFlow(BaseModel):
    wid = BigIntegerField()
    name = CharField()
    order = IntegerField()
    create_at = DateTimeField(
        constraints=[SQL("DEFAULT (datetime('now'))")],
        default=datetime.datetime.now().replace(microsecond=0)
    )

    class Meta:
        db_table = 'work_flow'
        indexes = (
            (('wid', 'order'), True),
        )


class WorkFlowBO:
    work_flow = None
    work_operates = []


class WorkMonitor(BaseModel):
    wid = BigIntegerField()
    name = CharField()
    create_at = DateTimeField(
        constraints=[SQL("DEFAULT (datetime('now'))")],
        default=datetime.datetime.now().replace(microsecond=0)
    )

    class Meta:
        db_table = 'work_monitor'


class WorkMonitorBO:
    work_monitor = None
    work_operate = []


class WorkOperate(BaseModel):
    fm_id = BigIntegerField()
    fm_type = IntegerField()
    op_type = IntegerField()
    op_content = CharField()
    order = IntegerField()
    create_at = DateTimeField(
        constraints=[SQL("DEFAULT (datetime('now'))")],
        default=datetime.datetime.now().replace(microsecond=0)
    )

    class Meta:
        db_table = 'work_operate'
        indexes = (
            (('fm_id', 'fm_type', 'order'), True),
        )


@unique
class FMTypeEnum(Enum):
    FLOW = 1
    MONITOR = 2
