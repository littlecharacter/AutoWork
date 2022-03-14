import tkinter as tk
import tkinter.ttk as ttk


# 初始化窗口宽高
S_WIDTH = 500
S_HEIGHT = 300




class AutoWork:
    def __init__(self, master=None):
        # build ui
        self.mainWin = tk.Tk()
        self.mainFrame = tk.Frame(self.mainWin, bg='blue')

        self.mainWin.bind('<Configure>', self.handle_resize)

    def handle_resize(self, event=None):
        widget = event.widget
        widget.update()
        self.mainFrame.configure(height=f'{widget.winfo_height()}', width=f'{widget.winfo_width()}')
        self.mainFrame.pack()

    def run(self):
        self.mainWin.mainloop()

    def add(self):
        pass

    def refresh(self):
        pass


if __name__ == '__main__':
    app = AutoWork()
    app.run()
