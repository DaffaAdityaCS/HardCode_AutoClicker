import pyautogui
#taking screenshot on the region of choice
iml = pyautogui.screenshot(region=(640,350,630,450))
#save it on the directory
iml.save(r"D:\programing\Project\python bot\saveimage.png")
