# https://www.jianshu.com/p/ba8a27cf7da1
# https://www.cnblogs.com/goldsunshine/p/15259246.html
import sqlite3
import peewee
import datetime
import core.orm as orm

db = peewee.SqliteDatabase('../db/auto_work.db')


class BaseModel(peewee.Model):
    class Meta:
        database = db


class WorkItem(BaseModel):
    name = peewee.CharField()
    create_at = peewee.DateTimeField(default=datetime.datetime.now())
    work_operate = []

    class Meta:
        db_table = 'work_item'


class WorkOperate(BaseModel):
    op_type = peewee.IntegerField()
    op_content = peewee.CharField()
    order = peewee.IntegerField()


def test_insert_record():
    WorkItem.create_table()
    work_item = WorkItem()
    # work_item.id = 2
    work_item.name = '人族无敌'
    work_item.save()
    pass


def test_select_record():
    WorkItem.create_table()
    works = list(WorkItem.select().order_by(WorkItem.id.desc()))
    print(works)
    for work in works:
        print(f"id={work.id},name={work.name},time={work.create_at}")
    for work in works:
        work.work_operate.append(WorkOperate(op_type=1, op_content='123', order=2))
        print(work.name)
        for operate in work.work_operate:
            print(operate.op_content)
    work_items = list(WorkItem.select().where(WorkItem.name == '人族无敌').order_by(WorkItem.id.desc()))
    for work_item in work_items:
        print(f"id={work_item.id},name={work_item.name}")
    pass


def test_update_record():
    WorkItem.create_table()
    works = WorkItem.select()
    for work in works:
        if work.id == 2:
            work.name = '人族无敌呀'
            work.save()
    pass


def test_delete_record():
    WorkItem.create_table()
    # 删除姓名为perter的数据
    WorkItem.delete().where(WorkItem.id > 3).execute()

    # 已经实例化的数据, 使用delete_instance
    work_item = WorkItem(id=3)
    work_item.delete_instance()
    pass


if __name__ == "__main__":
    pass

    # test_insert_record()
    # test_select_record()
    # test_update_record()
    # test_delete_record()

    # 新增工作项
    # work_item = orm.WorkItem(name='自动发送消息')
    # orm.insert_work_item(work_item)
    # 新增工作流程
    # work_flow = orm.WorkFlow(wid=1, name='按回车发消息', order=6)
    # orm.insert_work_flow(work_flow)
    # 查询工作流程
    # orm.select_work_flows(1)
    # 查询工作监控
    # orm.select_work_monitors(1)
    # 新增工作操作
    # work_operate = orm.WorkOperate(fm_id=1, fm_type=1, op_type=10, op_content='/Applications/微信.app', order=1)
    # orm.insert_work_operate(work_operate)
    work_operate = orm.WorkOperate(fm_id=7, fm_type=1, op_type=10, op_content='/Applications/微信.app', order=1)
    orm.insert_work_operate(work_operate)
