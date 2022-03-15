import pyautogui
import tkinter as tk
from tkinter import ttk
from tkinter import *
from core.execute import *


class Window:
    def __init__(self):
        # build ui
        self.root = tk.Tk()
        self.root.title("Auto Work")
        self.root.geometry(f"{int(pyautogui.size()[0] / 3)}"
                           f"x{int(pyautogui.size()[1] / 3)}"
                           f"+{int(pyautogui.size()[0] / 2) - int(pyautogui.size()[0] / 6)}"
                           f"+{int(pyautogui.size()[1] / 2) - int(pyautogui.size()[1] / 6)}")
        MainFrame(self.root)

    def run(self):
        self.root.mainloop()


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
        tk.Button(self.frame_top, text='新建', command=self.add, fg='blue', relief=GROOVE).grid(row=0, column=0,
                                                                                              sticky='nsew')
        tk.Button(self.frame_top, text='刷新', command=self.refresh, fg='blue', relief=RIDGE).grid(row=0, column=1,
                                                                                                 sticky='nsew')
        self.frame_top.grid(row=0, column=0, sticky='nsew')
        # 2.数据区
        self.frame_bottom = tk.Frame(self.root)
        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.rowconfigure(0, weight=1)
        # 2.1TreeView
        columns = ("name", "operate")
        headers = ("姓名", "操作")
        self.tv = ttk.Treeview(self.frame_bottom, show="headings", columns=columns)
        for (column, header) in zip(columns, headers):
            self.tv.column(column, anchor="w")
            self.tv.heading(column, text=header, anchor="w")
        self.tv.grid(row=0, column=0, sticky='nsew')
        self.refresh()
        self.frame_bottom.grid(row=1, column=0, sticky='nsew')

    def refresh(self):
        contacts = [
            (1, '最后的防守'),
            (2, '人族无敌'),
        ]
        for i, person in enumerate(contacts):
            self.tv.insert('', i, values=(person[1]), iid=person[0])

    def add(self):
        self.frame_top.destroy()
        self.frame_bottom.destroy()
        BuildFrame(self.root)


class BuildFrame:
    def __init__(self, root):
        self.root = root
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=True, fill=BOTH)
        # 工作流程选项卡
        tab_flow = tk.Frame(self.tab_control, bg='red')
        tab_flow.rowconfigure(0, weight=1)
        tab_flow.columnconfigure(0, weight=1)
        tab_flow.columnconfigure(1, weight=1)
        tab_flow.columnconfigure(2, weight=1)
        columns = ("item", "operate")
        tv = ttk.Treeview(tab_flow, show="headings", columns=columns)
        tv.grid(row=0, column=0, columnspan=3, sticky='nsew')
        tk.Button(tab_flow, text='新增', command=self.add, fg='blue').grid(row=1, column=0, sticky='nsew')
        tk.Button(tab_flow, text='保存', command=self.save, fg='blue').grid(row=1, column=1, sticky='nsew')
        tk.Button(tab_flow, text='关闭', command=self.close, fg='blue').grid(row=1, column=2, sticky='nsew')
        self.tab_control.add(tab_flow, text='工作流程')
        # 工作监控选项卡
        tab_monitor = tk.Frame(self.tab_control, bg='blue')
        self.tab_control.add(tab_monitor, text='工作监控')

        self.tab_control.select(tab_flow)

    def add(self):
        mt_thread = MonitorThread(1, "监控线程")
        mt_thread.setDaemon(True)
        mt_thread.start()

    def save(self):
        self.tab_control.destroy()
        MainFrame(self.root)

    def close(self):
        self.tab_control.destroy()
        MainFrame(self.root)
