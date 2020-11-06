from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#timer before code start
time.sleep(1)

#def for mouse click
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#color of center: (255, 219, 195)
while keyboard.is_pressed('q') == False:

    #taking a screenshot in the region and save it has pic
    pic = pyautogui.screenshot(region=(640,350,630,450))
    #the width and height of pic on screenshot
    width, height = pic.size
    
    #look for every 5 pixel in range in width and height
    for x in range(0,width,5):
        for y in range(0,height,5):
            #the color in each pixel
            r,g,b = pic.getpixel((x,y))
            #look to blue pixel has a value 195 and click the pixel 
            if b == 195 :
                # x and y is width and height of monitor + the center of the box of gameplay for me in 640 and 350
                click(x + 640,y + 350)
                time.sleep(0.05)
                break
