# Automated cursor that drops the front screen, and utilizes whatever is next in line.
# By: Bryan Burnett
# On: Feb 19, 2024


# import libs and modules
import time
import pyautogui
import win32gui, win32con
import os

# pause for (10) seconds before execution
time.sleep(10)

# Set window to minimize - use next screen availible.
Minimize = win32gui.GetForegroundWindow() 
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)

# set x to instantiate the cycle to resume normal activity.
x = 1

# move the cursor 
while x == 1:
    pyautogui.moveTo(1000, 1000, duration = 120)
# give some time to exit
    time.sleep(30)
# repeat
    pyautogui.moveTo(500,500, duration = 120)
    time.sleep(30)
    pyautogui.moveTo(1000, 1000, duration = 120)
    time.sleep(30)
    pyautogui.moveTo(500,500, duration = 120)
    time.sleep(30)


## Changing from moveRel to moveTo for smoother on screen curser motion.
#    #pyautogui.moveRel(100, duration = 10)
## give some time to rest/stop program if needed.    
#    time.sleep(10)
## move the cursor some more
#    pyautogui.moveRel(-500, duration = 5)
#    time.sleep(10)
#    pyautogui.moveRel(-300, duration = 5)
#    time.sleep(10)
#    pyautogui.moveRel(-300, duration = 5)
#    time.sleep(10)
#    pyautogui.moveRel(-500, duration = 5)
#    time.sleep(10)
#    pyautogui.moveRel(-300, duration = 5)
#    time.sleep(10)

## Changing from the moveTo to the moveRel to avoid getting stuck in the mouse transition.
# move mouse to 1000, 1000
##pyautogui.moveTo(1000, 1000, duration = 60)
##pyautogui.moveTo(500,500, duration = 30)

## changing from the dragRel to the moveTo to avoid highlighting all everything the mouse touches.
## drags mouse 100, 0 from it's position
#pyautogui.dragRel(100, 0, duration = 1)
## drags mouse more
#pyautogui.dragRel(0, 100, duration = 1)
#pyautogui.dragRel(-100, 0 , duration = 1)
#pyautogui.dragRel(0, -100, duration = 1)