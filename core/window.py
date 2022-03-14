import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import *


class MainFrame:
    def __init__(self, root):
        self.root = root
        self.root.rowconfigure(0, weight=0)
        self.root.rowconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        # 1.按钮区
        self.frame_top = tk.Frame(self.root)
        self.frame_top.columnconfigure(0, weight=1)
        self.frame_top.columnconfigure(1, weight=1)
        tk.Button(self.frame_top, text='新建', command=self.add, fg='blue').grid(row=0, column=0, sticky='nsew')
        tk.Button(self.frame_top, text='刷新', command=self.refresh, fg='blue').grid(row=0, column=1, sticky='nsew')
        self.frame_top.grid(row=0, column=0, sticky='nsew')
        # 2.数据区
        self.frame_bottom = tk.Frame(self.root)
        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.rowconfigure(0, weight=1)
        # 2.1TreeView
        columns = ("name", "tel", "email", "company")
        headers = ("姓名", "电话", "邮箱", "公司")
        widths = (120, 120, 250, 250)
        self.tv = ttk.Treeview(self.frame_bottom, show="headings", columns=columns)
        for (column, header, width) in zip(columns, headers, widths):
            self.tv.column(column, width=width, anchor="w")
            self.tv.heading(column, text=header, anchor="w")
        self.tv.grid(row=0, column=0, sticky='nsew')
        self.refresh()
        self.frame_bottom.grid(row=1, column=0, sticky='nsew')

    def refresh(self):
            contacts = [
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
                ('张三', '1870591xxxx', 'zhang@qq.com', '腾讯'),
                ('李斯', '1589928xxxx', 'lisi@google.com', '谷歌'),
                ('王武', '1340752xxxx', 'wangwu@baidu.com', '微软'),
                ('麻溜儿', '1361601xxxx', 'maliur@alibaba.com', '阿里'),
                ('郑和', '1899986xxxx', 'zhenghe@163.com', '网易'),
            ]
            for i, person in enumerate(contacts):
                self.tv.insert('', i, values=person)

    def add(self):
        self.frame_top.destroy()
        self.frame_bottom.destroy()


class AutoWork:
    def __init__(self):
        # build ui
        self.root = tk.Tk()
        self.root.title("Auto Work")
        self.root.geometry(f"{int(pyautogui.size()[0] / 3)}x{int(pyautogui.size()[1] / 3)}+{int(pyautogui.size()[0] / 2) - 250}+{int(pyautogui.size()[1] / 2) - 150}")
        MainFrame(self.root)

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    app = AutoWork()
    app.run()
