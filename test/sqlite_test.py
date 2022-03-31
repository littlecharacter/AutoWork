# https://www.cnblogs.com/goldsunshine/p/15259246.html
import sqlite3
import pathlib

# 数据库文件的路径和文件名称
db = pathlib.PurePath("../db", "auto_work.db")


def test_create_database():
    # 创建连接
    conn = sqlite3.connect(db)
    # 创建游标
    cur = conn.cursor()
    # 定义要执行的SQL语句
    sql = '''CREATE TABLE work_item(
            id INT PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            phone INT NOT NULL
           )'''
    # 执行SQL
    try:
        cur.execute(sql)
        print("创建成功")
    except Exception as e:
        print("创建失败")
        print(f"失败原因是：{e}")
    finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        conn.close()


def test_insert_record():
    # 创建连接
    conn = sqlite3.connect(db)
    # 创建游标
    cur = conn.cursor()
    # 定义要执行的SQL语句
    sql = '''INSERT INTO work_item
              VALUES (?, ?, ?)'''
    v = (1, "Tom", 12377778888)
    # 执行SQL
    try:
        cur.execute(sql, v)
        conn.commit()
    except Exception as e:
        print(f"失败原因是：{e}")
    finally:
        # 关闭游标
        cur.close()
        # 关闭连接
        conn.close()


def test_select_record():
    pass


def test_update_record():
    pass


def test_delete_record():
    pass


if __name__ == "__main__":
    pass
    test_create_database()
    test_insert_record()
    test_select_record()
    test_update_record()
    test_delete_record()
