import pyautogui
import time


# find overwatch window

window = pyautogui.getWindowsWithTitle("Overwatch")[0]
if(window):
    # bring window to front
    window.minimize()
    window.maximize()
    
    # determine what map is being played
    
    # macro to position correctly on map

    # start controlling camera to center each hero


else:
    print("Overwatch not found.")







