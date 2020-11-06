from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#tile 1: X: 598 Y:  711 RGB: (253,  18,   1)
#tile 2: X: 687 Y:  719 RGB: (160, 165, 232)
#tile 3: X:  792 Y:  718 RGB: (180, 183, 235)
#tile 4: X:  884 Y:  716 RGB: (168, 172, 232)

#Make def mouse click
def click(x,y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
#emergency stop system
while keyboard.is_pressed("q") == False:
    #look every individual tale on the screen
    if pyautogui.pixel(587, 673)[0] == 0:
        click(587, 673)
    elif pyautogui.pixel(672, 676)[0] == 0:
        click(672, 676)
    elif pyautogui.pixel(776, 678)[0] == 0:
        click(776, 678)
    elif pyautogui.pixel(869, 673)[0] == 0:
        click(869, 673)
