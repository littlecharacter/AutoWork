import pyautogui
import cv2
import pyscreeze

# 屏幕缩放系数 mac缩放是2 windows一般是1
screenScale = pyautogui.screenshot().size[0] / pyautogui.size()[0]
# print(pyautogui.size())
print(f"屏幕缩放系数：{screenScale}")

# 事先读取按钮截图
target = cv2.imread(r"../img/db.png", cv2.IMREAD_GRAYSCALE)
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
print(f"minVal:{minVal},maxVal:{maxVal},minLoc:{minLoc},maxLoc:{maxLoc}")
if maxVal >= 0.9:
    # 计算出中心点(因为截图就是原图，所以这里要缩放)
    tagHalfW = int(targetWidth / screenScale / 2)
    tagHalfH = int(targetHeight / screenScale / 2)
    tagCenterX = maxLoc[0] / screenScale + tagHalfW
    tagCenterY = maxLoc[1] / screenScale + tagHalfH
    # 左键点击屏幕上的这个位置
    print(f"tagCenterX:{tagCenterX},tagCenterY:{tagCenterY}")
    pyautogui.click(tagCenterX, tagCenterY, button='left')
else:
    print("没找到")
