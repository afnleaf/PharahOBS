import pyautogui
import pydirectinput
import time

# Antarctic Peninsula
def antarctic_icebreaker():
    return

def antarctic_labs():
    return

def antarctic_sublevel():
    return

# Busan
def busan_mekabase():
    return

def busan_sanctuary():
    return

def busan_downtown():
    return

# Ilios
def ilios_lighthouse():
    return

def ilios_ruins():
    return

def ilios_well():
    return

# Lijiang Tower
def lijiang_controlcenter():
    return

def lijiang_gardens():
    return
    
def lijiang_nightmarket():
    return

# Nepal
def nepal_sanctum():
    return
    
def nepal_shrine():
    return

def nepal_village():
    return
    
# Oasis
def oasis_citycenter():
    return

def oasis_gardens():
    return

def oasis_university():
    return


# Samoa
def samoa_beach():
    return

def samoa_downtown():
    return
    
def samoa_volcano():
    return

# flashpoint
def newjunkcity():
    return

def suravasa():
    return

# hybrid
def blizzardworld():
    return

def eichenwalde():
    return

def hollywood():
    return

def kingsrow():
    return

def midtown():
    return

def numbani():
    return

def paraiso():
    return

# escort
def circuitroyal():
    return

def dorado():
    return

def havana():
    return

def junkertown():
    return
    
def rialto():
    return

def route66():
    return

def shambali():
    return

def gibraltar():
    return


# push
def colosseo():
    window = pyautogui.getWindowsWithTitle("Overwatch")[0]
    if(window):
        # bring window to front
        window.minimize()
        window.maximize()
        pyautogui.click()
        pyautogui.hotkey("ctrl", "i")
        # move up
        pyautogui.keyDown("shift")
        pyautogui.keyDown("e")
        time.sleep(4)
        pyautogui.keyUp("e")
        pyautogui.keyUp("shift")
        # move right
        pyautogui.keyDown("shift")
        pyautogui.keyDown("d")
        time.sleep(0.3)
        pyautogui.keyUp("d")
        pyautogui.keyUp("shift")
        # move back
        pyautogui.keyDown("shift")
        pyautogui.keyDown("s")
        time.sleep(0.4)
        pyautogui.keyUp("s")
        pyautogui.keyUp("shift")
        # move camera down
        pydirectinput.moveTo(0, 80)
        #pydirectinput.move(100, None)
        
    else:
        print("Overwatch not found.")
    return

def esperanca():
    window = pyautogui.getWindowsWithTitle("Overwatch")[0]
    if(window):
        # bring window to front
        window.minimize()
        window.maximize()
        pyautogui.click()
        pyautogui.hotkey("ctrl", "i")
        # move up
        pyautogui.keyDown("shift")
        pyautogui.keyDown("e")
        time.sleep(3.5)
        pyautogui.keyUp("e")
        pyautogui.keyUp("shift")
        # move forward
        pyautogui.keyDown("shift")
        pyautogui.keyDown("w")
        pyautogui.keyDown("d")
        time.sleep(0.7)
        pyautogui.keyUp("w")
        pyautogui.keyUp("d")
        pyautogui.keyUp("shift")
        # move camera down
        pydirectinput.moveTo(0, 100)
        pydirectinput.move(200, None)
        pydirectinput.move(50, None)
    else:
        print("Overwatch not found.")
    return

def newqueenstreet():
    window = pyautogui.getWindowsWithTitle("Overwatch")[0]
    if(window):
        # bring window to front
        window.minimize()
        window.maximize()
        pyautogui.click()
        pyautogui.hotkey("ctrl", "i")
        # move up
        pyautogui.keyDown("shift")
        pyautogui.keyDown("e")
        time.sleep(3)
        pyautogui.keyUp("e")
        pyautogui.keyUp("shift")
        # move forward
        pyautogui.keyDown("shift")
        pyautogui.keyDown("s")
        time.sleep(1)
        pyautogui.keyUp("s")
        pyautogui.keyUp("shift")
        # move camera down
        pydirectinput.moveTo(0, 40)        
    else:
        print("Overwatch not found.")
    return
    return