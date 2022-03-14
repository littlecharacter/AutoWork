import tkinter as tk

win = tk.Tk()
win.title("C语言中文网")
win.geometry('400x350+200+200')
win.iconbitmap('C:/Users/Administrator/Desktop/C语言中文网logo.ico')
win.rowconfigure(1, weight=1)
win.columnconfigure(0, weight=1)

# 左侧的frame
frame_left = tk.LabelFrame(win, bg='red')
tk.Label(frame_left, text='左侧标签1', bg='green', width=10, height=5).grid(row=0, column=0)
tk.Label(frame_left, text='左侧标签2', bg='blue', width=10, height=5).grid(row=1, column=1)
frame_left.grid(row=0, column=0)

# 右侧的frame
frame_right = tk.LabelFrame(win, bg='yellow')
tk.Label(frame_right, text='右侧标签1', bg='gray', width=10, height=5).grid(row=0, column=1)
tk.Label(frame_right, text='右侧标签2', bg='pink', width=10, height=5).grid(row=1, column=0)
tk.Label(frame_right, text='右侧标签3', bg='purple', width=10, height=5).grid(row=1, column=1)
frame_right.grid(row=1, column=0)

frame_left.columnconfigure(2, weight=1)
frame_right.rowconfigure(0, weight=1)
frame_right.columnconfigure(0, weight=1)

win.mainloop()
