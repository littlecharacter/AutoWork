import datetime
import tkinter as tk
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
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
        s = ttk.Style()
        s.configure('Treeview', rowheight=30)
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
        tk.Button(self.frame_top, text='新建', command=self.add_work, fg='blue', relief=GROOVE).grid(row=0, column=0, sticky='nsew')
        tk.Button(self.frame_top, text='刷新', command=self.refresh, fg='blue', relief=RIDGE).grid(row=0, column=1, sticky='nsew')
        self.frame_top.grid(row=0, column=0, sticky='nsew')
        # 2.数据区
        self.frame_bottom = tk.Frame(self.root)
        self.frame_bottom.columnconfigure(0, weight=1)
        self.frame_bottom.rowconfigure(0, weight=1)
        # 2.1TreeView
        columns = ("name", "status")
        headers = ("作业", "状态")
        self.tv = ttk.Treeview(self.frame_bottom, show="headings", columns=columns)
        for (column, header) in zip(columns, headers):
            self.tv.column(column, anchor="w")
            self.tv.heading(column, text=header, anchor="w")
        self.tv.grid(row=0, column=0, sticky='nsew')
        self.tv.bind('<Button-2>', self.show_menu)
        self.refresh()
        self.frame_bottom.grid(row=1, column=0, sticky='nsew')
        # 2.2右键菜单
        self.menu = tk.Menu(self.tv, tearoff=False)
        self.menu.add_command(label="运行", command=self.start_work)
        self.menu.add_command(label="停止", command=self.stop_work)
        self.menu.add_command(label="查看", command=self.show_work)
        # menu.add_command(label="修改", command=func)
        # menu.add_command(label="删除", command=func)

    def refresh(self):
        # 先清空数据
        x = self.tv.get_children()
        for item in x:
            self.tv.delete(item)
        # 再插入数据
        work_list = get_all_data(WORK_FILENAME)
        if work_list:
            for work_dict in work_list:
                if run_flag.full() and work_dict.get('wid') == run_work.get('wid'):
                    self.tv.insert('', 'end', values=(work_dict.get('name'), "运行"), iid=work_dict.get('wid'))
                else:
                    self.tv.insert('', 'end', values=(work_dict.get('name'), "停止"), iid=work_dict.get('wid'))

    def add_work(self):
        self.frame_top.destroy()
        self.frame_bottom.destroy()
        BuildFrame(self.root, ActionEnum.ADD)

    def show_menu(self, event):
        item = self.tv.identify_row(event.y)
        self.tv.selection_set(item)
        self.menu.post(event.x_root, event.y_root)

    def start_work(self):
        if run_flag.full():
            mb.askokcancel("提示", "作业正在运行，请先停止！")
            return
        item = self.tv.selection()
        if item:
            wt_thread = WorkThread(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S')), "工作线程")
            wt_thread.wid = int(item[0])
            wt_thread.setDaemon(True)
            wt_thread.start()
            self.refresh()

    def stop_work(self):
        item = self.tv.selection()
        if run_flag.full() and int(item[0]) == run_work.get('wid'):
            stop_signal.put_nowait(1)
            time.sleep(1)
            self.refresh()
        else:
            mb.askokcancel("提示", "该任务未运行，无需停止！")

    def show_work(self):
        item = self.tv.selection()
        self.frame_top.destroy()
        self.frame_bottom.destroy()
        BuildFrame(self.root, ActionEnum.SHOW, item[0])


class BuildFrame:
    def __init__(self, root, action, wid=None):
        self.root = root
        self.action = action
        self.wid = wid
        self.tab_control = ttk.Notebook(self.root)
        self.tab_control.pack(expand=True, fill=BOTH)
        # 工作流程选项卡
        tab_flow = tk.Frame(self.tab_control)
        tab_flow.rowconfigure(0, weight=1)
        tab_flow.columnconfigure(0, weight=1)
        flow_columns = ("step", "name")
        flow_headers = ("步骤", "名称")
        self.flow_tv = ttk.Treeview(tab_flow, show="headings", columns=flow_columns)
        for (column, header) in zip(flow_columns, flow_headers):
            self.flow_tv.column(column, anchor="w")
            self.flow_tv.heading(column, text=header, anchor="w")
        if self.action == ActionEnum.ADD:
            tab_flow.columnconfigure(1, weight=1)
            self.flow_tv.grid(row=0, column=0, columnspan=2, sticky='nsew')
            tk.Button(tab_flow, text='插入', command=self.insert_flow, fg='blue', state=DISABLED).grid(row=1, column=0, sticky='nsew')
            tk.Button(tab_flow, text='关闭', command=self.close, fg='blue').grid(row=1, column=1, sticky='nsew')
        elif self.action == ActionEnum.SHOW or self.action == ActionEnum.MODIFY:
            self.flow_tv.grid(row=0, column=0, sticky='nsew')
            tk.Button(tab_flow, text='返回', command=self.close, fg='blue').grid(row=1, column=0, sticky='nsew')
            if self.action == ActionEnum.MODIFY:
                # 右键菜单
                self.flow_menu = tk.Menu(self.flow_tv, tearoff=False)
                self.flow_menu.add_command(label="查看", command=self.show_flow_item)
                self.flow_menu.add_command(label="修改", command=self.modify_flow_item)
                self.flow_menu.add_command(label="删除", command=self.delete_flow_item)
                self.flow_tv.bind('<Button-2>', self.show_flow_menu)
            self.show_flow()
        self.tab_control.add(tab_flow, text='作业流程')
        # 工作监控选项卡
        tab_monitor = tk.Frame(self.tab_control)
        tab_monitor.rowconfigure(0, weight=1)
        tab_monitor.columnconfigure(0, weight=1)
        monitor_columns = ("name",)
        monitor_headers = ("监控项",)
        self.monitor_tv = ttk.Treeview(tab_monitor, show="headings", columns=monitor_columns)
        for (column, header) in zip(monitor_columns, monitor_headers):
            self.monitor_tv.column(column, anchor="w")
            self.monitor_tv.heading(column, text=header, anchor="w")
        if self.action == ActionEnum.ADD:
            tab_monitor.columnconfigure(1, weight=1)
            self.monitor_tv.grid(row=0, column=0, columnspan=2, sticky='nsew')
            tk.Button(tab_monitor, text='插入', command=self.insert_monitor, fg='blue', state=DISABLED).grid(row=1, column=0, sticky='nsew')
            tk.Button(tab_monitor, text='关闭', command=self.close, fg='blue').grid(row=1, column=1, sticky='nsew')
        elif self.action == ActionEnum.SHOW or self.action == ActionEnum.MODIFY:
            self.monitor_tv.grid(row=0, column=0, sticky='nsew')
            tk.Button(tab_monitor, text='返回', command=self.close, fg='blue').grid(row=1, column=0, sticky='nsew')
            if self.action == ActionEnum.MODIFY:
                # 右键菜单
                self.monitor_menu = tk.Menu(self.monitor_tv, tearoff=False)
                self.monitor_menu.add_command(label="查看", command=self.show_monitor_item)
                self.monitor_menu.add_command(label="修改", command=self.modify_monitor_item)
                self.monitor_menu.add_command(label="删除", command=self.delete_monitor_item)
                self.monitor_tv.bind('<Button-2>', self.show_monitor_menu)
            self.show_monitor()
        self.tab_control.add(tab_monitor, text='作业监控')
        self.tab_control.select(tab_flow)

    def show_flow_menu(self, event):
        item = self.flow_tv.identify_row(event.y)
        self.flow_tv.selection_set(item)
        self.flow_menu.post(event.x_root, event.y_root)

    def show_monitor_menu(self, event):
        item = self.monitor_tv.identify_row(event.y)
        self.monitor_tv.selection_set(item)
        self.monitor_menu.post(event.x_root, event.y_root)

    def show_flow(self):
        # 先清空数据
        x = self.flow_tv.get_children()
        for item in x:
            self.flow_tv.delete(item)
        # 再插入数据
        flow_dict = get_special_data(self.wid, FLOW_FILENAME)
        if flow_dict:
            flow_item_list = flow_dict.get('flow')
            for flow_item_dict in flow_item_list:
                self.flow_tv.insert('', 'end', values=(f"第{flow_item_dict.get('fid') + 1}步", flow_item_dict.get('name')), iid=flow_item_dict.get('fid'))

    def show_monitor(self):
        # 先清空数据
        x = self.monitor_tv.get_children()
        for item in x:
            self.monitor_tv.delete(item)
        # 再插入数据
        monitor_dict = get_special_data(self.wid, MONITOR_FILENAME)
        if monitor_dict:
            monitor_item_list = monitor_dict.get('monitor')
            for monitor_item_dict in monitor_item_list:
                self.monitor_tv.insert('', 'end', values=(monitor_item_dict.get('name')), iid=monitor_item_dict.get('mid'))

    def show_flow_item(self):
        item = self.flow_tv.selection()
        if item:
            print(f"{item} show...")

    def show_monitor_item(self):
        item = self.monitor_tv.selection()
        if item:
            print(f"{item} show...")

    def modify_flow_item(self):
        item = self.flow_tv.selection()
        if item:
            print(f"{item} modify...")

    def modify_monitor_item(self):
        item = self.monitor_tv.selection()
        if item:
            print(f"{item} modify...")

    def delete_flow_item(self):
        item = self.flow_tv.selection()
        if item:
            print(f"{item} delete...")

    def delete_monitor_item(self):
        item = self.monitor_tv.selection()
        if item:
            print(f"{item} delete...")

    def insert_flow(self):
        pass

    def insert_monitor(self):
        pass

    def close(self):
        self.tab_control.destroy()
        MainFrame(self.root)


@unique
class ActionEnum(Enum):
    ADD = 1
    MODIFY = 2
    SHOW = 3
