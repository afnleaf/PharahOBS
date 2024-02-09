import pyautogui
import pydirectinput # needed to move mouse
import time


# find overwatch window

window = pyautogui.getWindowsWithTitle("Overwatch")[0]
if(window):
    # bring window to front
    window.minimize()
    window.maximize()
    
    # determine if mode is live scrim or code
    # we start with replay codes
    # check if game is unpaused or paused
    game_paused = True
    if(game_paused):
        pyautogui.press("space")
    # check if overlay is on
    overlay_on = False
    if(not overlay_on):
        pyautogui.hotkey("ctrl", "i")
        
    # determine what map is being played
    # macro to position correctly on map
    # make sure overlay is on
    # start controlling camera to center each hero

    # let make a fake loop to just move the camera around randomly?
    # controls
    # wasd (directiona) 
    # e (up)
    # q (down)
    # ctrl (slow)
    # shift (fast)
    # mouse dragto random positions
    #timeout = 20 # num seconds
    #timeout_start = time.time()
    #while time.time() < timeout_start + timeout:

    pyautogui.click()
    pyautogui.keyDown("shift")
    pyautogui.keyDown("e")
    time.sleep(2)
    pyautogui.keyUp("e")
    pyautogui.keyUp("shift")
    #pyautogui.dragTo(0, -100)
    pydirectinput.moveTo(0, 25)






else:
    print("Overwatch not found.")







