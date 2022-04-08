import os
import cv2
import pyautogui
import pyscreeze
from core.execute import *

pyautogui.FAILSAFE = False

IMG_PATH = '../img/'


def test_mouse():
    for i in range(10):
        pyautogui.moveTo(x=0, y=0, duration=0.25)
    # x, y = pyautogui.position()
    # pyautogui.moveTo(x=x-100, y=y+100, duration=0.25)
    # x, y = pyautogui.position()
    # pyautogui.click(x, y, button='right')


if __name__ == "__main__":
    pass
    # print(platform.system().lower())
    # test_mouse()
    click_img(20220101000000, "database.png", 2)
