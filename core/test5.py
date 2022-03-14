import sys
import tkinter
import tkinter.ttk


def guiInit():
    top = tkinter.Tk()
    # 窗口大小和位置 WxH+X+Y
    # 窗口大小 宽800, 高480
    # 窗口位置 距左边200, 距上边100
    top.geometry('800x480+200+100')
    label1 = tkinter.ttk.Label(top, width=10, text='label1', relief='raised')
    label2 = tkinter.ttk.Label(top, width=10, text='label2', relief='raised')
    label3 = tkinter.ttk.Label(top, width=10, text='label3', relief='raised')
    label4 = tkinter.ttk.Label(top, width=10, text='label4', relief='raised')
    label5 = tkinter.ttk.Label(top, width=10, text='label5', relief='raised')
    label6 = tkinter.ttk.Label(top, width=10, text='label6', relief='raised')

    '''
    指定位置
        YourWidget.grip(row=N, column=N, sticky='nsew',
            rowspan=N, columnspan=N, padx=N, pady=N)
    指定大小: weight表示权重如果所有单元格全为1, 则表示等大小
        weight=0: YourWidget的实际大小，固定大小
        YourWidget.rowconfigure(N, weight=1)
        YourWidget.columnconfigure(N, weight=1)
    '''
    label1.grid(row=0, column=0, sticky='nsew')
    label2.grid(row=0, column=1, sticky='nsew')
    label5.grid(row=0, column=2, sticky='nsew', rowspan=2, padx=5, pady=5)
    label3.grid(row=1, column=0, sticky='nsew')
    label4.grid(row=1, column=1, sticky='nsew')
    label6.grid(row=2, column=0, sticky='nsew', columnspan=3)
    '''
    top.rowconfigure("all", weight=1)
    top.columnconfigure("all", weight=1)
    '''
    top.rowconfigure(0, weight=3)
    top.rowconfigure(1, weight=1)
    top.rowconfigure(2, weight=0)
    # top.columnconfigure([0, 1], weight=1)
    top.columnconfigure(0, weight=3)
    top.columnconfigure(1, weight=1)
    top.columnconfigure(2, weight=0)
    top.mainloop()


def main():
    guiInit()


if __name__ == '__main__':
    main()
