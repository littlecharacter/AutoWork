import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        position_str = f"x:{x},y:{y}"
        print("\r", position_str, end='', flush=True)
except KeyboardInterrupt:
    print('\n')



