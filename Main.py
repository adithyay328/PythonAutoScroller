import pyautogui
import time

while True:
    time.sleep(2)

    pyautogui.moveRel(100, 100, 5)

    time.sleep(4)

    pyautogui.scroll(5)

    time.sleep(4)

    pyautogui.scroll(-3)

    pyautogui.moveRel(-100, -100, 5)