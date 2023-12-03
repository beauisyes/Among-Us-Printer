import win32api
import win32print
import time
import pyautogui

def printAmongus():
    win32api.ShellExecute(0, 'print', 'amongus.png', f'/c:"{win32print.GetDefaultPrinter()}"', '.', 0)
    

    # Delay for a few seconds to allow time to position the mouse
    time.sleep(5)

    # Specify the coordinates where you want the mouse to move
    x_coordinate = 1190
    y_coordinate = 773

    # Move the mouse to the specified coordinates
    pyautogui.moveTo(x_coordinate, y_coordinate, duration=1)

    # Perform a left mouse click
    pyautogui.click()
