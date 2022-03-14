import tkinter
import pyautogui


class BaseFrame:
    def __init__(self):
        self.baseFrame = tkinter.Frame(mainWin, bg="yellow")
        self.baseFrame.pack()


class ControlFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.baseFrame.config(bg='blue')
        addButton = tkinter.Button(self.baseFrame, text="新增", command=self.add)
        # addButton.place(x=100, y=100)
        addButton.pack()

    # 设置回调函数
    def add(self):
        self.baseFrame.destroy()
        print("add")
        BuildFrame()


class BuildFrame(BaseFrame):
    def __init__(self):
        super().__init__()
        self.baseFrame.config(bg='red')
        backButton = tkinter.Button(self.baseFrame, text="返回", command=self.back)
        # backButton.place(x=225, y=125)
        backButton.pack()

    # 设置回调函数
    def back(self):
        self.baseFrame.destroy()
        print("back")
        ControlFrame()


if __name__ == '__main__':
    mainWin = tkinter.Tk()
    mainWin.title("Auto Work")
    # window.iconbitmap(icon文件)
    mainWin.iconbitmap()
    # window.geometry("宽x高+X+Y")
    mainWin.geometry(f"500x300+{int(pyautogui.size()[0] / 2) - 250}+{int(pyautogui.size()[1] / 2) - 150}")
    # 载入控制框架
    ControlFrame()
    mainWin.mainloop()
