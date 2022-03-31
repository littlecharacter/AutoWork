import cv2
import pyautogui
import pyscreeze


pyautogui.FAILSAFE = False


def test_mouse():
    for i in range(10):
        pyautogui.moveTo(x=0, y=0, duration=0.25)
    # x, y = pyautogui.position()
    # pyautogui.moveTo(x=x-100, y=y+100, duration=0.25)
    # x, y = pyautogui.position()
    # pyautogui.click(x, y, button='right')


def locate_img(wid, op_content):
    while True:
        # 屏幕缩放系数 mac缩放是2 windows一般是1
        screenScale = pyautogui.screenshot().size[0] / pyautogui.size()[0]
        # print(pyautogui.size())
        print(f"屏幕缩放系数：{screenScale}")

        # 事先读取按钮截图
        img_path = f"../img/{wid}/{op_content}"
        target = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        targetHeight, targetWidth = target.shape[:2]

        # 先截图
        screenshot = pyscreeze.screenshot('../img/screenshot.png')
        # 读取图片 灰色会快
        source = cv2.imread(r'../img/screenshot.png', cv2.IMREAD_GRAYSCALE)
        # sourceHeight, sourceWidth = source.shape[:2]
        # 先缩放屏幕截图(本程序中无需缩放，因为截图就是原图)
        # sourceScale = cv2.resize(source, (int(sourceWidth / screenScale), int(sourceHeight / screenScale)), interpolation=cv2.INTER_AREA)
        # print(sourceScale.shape[:2])

        # 匹配图片
        matchResult = cv2.matchTemplate(source, target, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(matchResult)
        # print(f"minVal:{minVal},maxVal:{maxVal},minLoc:{minLoc},maxLoc:{maxLoc}")
        if maxVal >= 0.8:
            # 计算出中心点(因为截图就是原图，所以这里要缩放)
            tagHalfW = int(targetWidth / screenScale / 2)
            tagHalfH = int(targetHeight / screenScale / 2)
            tagCenterX = maxLoc[0] / screenScale + tagHalfW
            tagCenterY = maxLoc[1] / screenScale + tagHalfH
            # 左键点击屏幕上的这个位置
            pyautogui.moveTo(x=tagCenterX, y=tagCenterY, duration=0.25)
            pyautogui.click()
            break
        else:
            print("没有匹配到")


if __name__ == "__main__":
    pass
    # print(platform.system().lower())
    # test_mouse()
    locate_img(20220101000000, "database.png")
