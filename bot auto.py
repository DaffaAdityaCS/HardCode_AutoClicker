from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('pk.png' ,region=(0,150,400,350), grayscale=True, confidence=0.7) != None:
        print ("pk")
        time.sleep(0.5)
    else :
        print("no pk")
        time.sleep(0.5)