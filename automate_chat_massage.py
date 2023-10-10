import pyautogui
import time

# 
text = "hello world"

counter = 5
while counter > 0:
    # time in seconds before the program starts
    time.sleep(2)
    # what prorgam writes
    pyautogui.typewrite(text)

    # program time before pressing enter
    time.sleep(2)

    #prorgam pressing enter 
    pyautogui.press('enter')

    counter -= 1
