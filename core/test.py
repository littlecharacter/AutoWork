import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("C语言中文网")
root.geometry('450x180+300+200')
root.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
# 创建一个滚动条控件，默认为垂直方向
sbar1 = tk.Scrollbar(root)
# 将滚动条放置在右侧，并设置当窗口大小改变时滚动条会沿着垂直方向延展
sbar1.pack(side=RIGHT, fill=Y)
# 创建水平滚动条，默认为水平方向,当拖动窗口时会沿着X轴方向填充
sbar2 = Scrollbar(root, orient=HORIZONTAL)
sbar2.pack(side=BOTTOM, fill=X)
# 创建列表框控件,并添加两个滚动条（分别在垂直和水平方向），使用 set() 进行设置
mylist = tk.Listbox(root, xscrollcommand=sbar2.set, yscrollcommand=sbar1.set)
for i in range(30):
    mylist.insert(END, '第' + str(i + 1) + '次:' + 'C语言中文网，网址为：c.biancheng.net' + '\n')
# 当窗口改变大小时会在X与Y方向填满窗口
mylist.pack(side=LEFT, fill=BOTH)
# 使用 command 关联控件的 yview、xview方法
sbar1.config(command=mylist.yview)
sbar2.config(command=mylist.xview)
#  显示主窗口
root.mainloop()
