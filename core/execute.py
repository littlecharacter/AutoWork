import threading
import time


class MonitorThread(threading.Thread):
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    # 把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
    def run(self):
        while True:
            print(f"name：{self.name}-{time.time()}")
            time.sleep(3)

