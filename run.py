# modules
import Replay
import Live

# select mode to use the tool in
def select_mode():
    while True:
        print("Select Mode:")
        print("(1) Replay Viewer")
        print("(2) Lobby Spectator")
        option = input("")
        if option in ['1', '2']:
            return int(option)

# select map type currently being played --------------------------------------
def select_map_type():
    while True:
        print("Select map type:")
        print("(1) Control")
        print("(2) Escort")
        print("(3) Flashpoint")
        print("(4) Hybrid")
        print("(5) Push")
        print("(6) Back")
        option = input("")

        # Validate user input
        if option in ['1', '2', '3', '4', '5', '6']:
            option = int(option)
            if option == 1:
                print("You selected Control.")
                select_control_map()
            elif option == 2:
                print("You selected Escort.")
                select_escort_map()
            elif option == 3:
                print("You selected Flashpoint.")
                select_flashpoint_map()
            elif option == 4:
                print("You selected Hybrid.")
                select_hybrid_map()
            elif option == 5:
                print("You selected Push.")
                select_push_map()
            elif option == 6:
                print("Returning to mode selection.")
                return  # Return to the caller
        else:
            print("Invalid input.")

# select control map name -----------------------------------------------------
def select_control_map():
    while True:
        print("Select control map:")
        print("(1) Antartic Peninsula")
        print("(2) Busan")
        print("(3) Ilios")
        print("(4) Lijiang Tower")
        print("(5) Nepal")
        print("(6) Oasis")
        print("(7) Samoa")
        print("(8) Back")
        option = input("")
        if option in ['1', '2', '3', '4', '5', '6', '7', '8']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                print("Antarctic Peninsula.")
                select_antarctic_submap()
            elif option == 2:
                print("Busan.")
                select_busan_submap()
            elif option == 3:
                print("Ilios.")
                select_ilios_submap()
            elif option == 4:
                print("Lijiang Tower")
                select_lijiang_submap()
            elif option == 5:
                print("Nepal.")
                select_nepal_submap()
            elif option == 6:
                print("Oasis.")
                select_oasis_submap()
            elif option == 7:
                print("Samoa")
                select_samoa_submap()
            elif option == 8:
                print("Back")
                return
        else:
            print("Invalid input.")


# control submaps -------------------------------------------------------------
def select_antarctic_submap():
    while True:
        print("Select Antarctic Peninsula submap:")
        print("(1) Icebreaker")
        print("(2) Labs")
        print("(3) Sublevel")
        print("(4) Back.")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                if mode == 1:
                    Replay.antarctic_icebreaker()
                elif mode == 2:
                    Live.antarctic_icebreaker()
            elif option == 2:
                if mode == 1:
                    Replay.antarctic_labs()
                elif mode == 2:
                    Live.antarctic_labs()
            elif option == 3:
                if mode == 1:
                    Replay.antarctic_sublevel()
                elif mode == 2:
                    Live.antarctic_sublevel()
            elif option == 4:
                print("back to control map.")
                return
    return

def select_busan_submap():
    while True:
        print("Select Busan submap:")
        print("(1) Downtown")
        print("(2) Meka Base")
        print("(3) Sanctuary")
        print("(4) Back.")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                if mode == 1:
                    Replay.busan_downtown()
                elif mode == 2:
                    Live.busan_downtown()
            elif option == 2:
                if mode == 1:
                    Replay.busan_mekabase()
                elif mode == 2:
                    Live.busan_mekabase()
            elif option == 3:
                if mode == 1:
                    Replay.busan_sanctuary()
                elif mode == 2:
                    Replay.busan_sanctuary()
            elif option == 4:
                print("back to control map.")
                return
    return

def select_ilios_submap():
    while True:
        print("Select Ilios submap:")
        print("(1) Lighthouse")
        print("(2) Ruins")
        print("(3) Well")
        print("(4) Back.")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                if mode == 1:
                    Replay.ilios_lighthouse()
                elif mode == 2:
                    Live.ilios_lighthouse()
            elif option == 2:
                if mode == 1:
                    Replay.ilios_ruins()
                elif mode == 2:
                    Live.ilios_ruins()
            elif option == 3:
                if mode == 1:
                    Replay.ilios_well()
                elif mode == 2:
                    Live.ilios_well()
            elif option == 4:
                print("back to control map.")
                return
    return

def select_lijiang_submap():
    while True:
        print("Select Lijiang Tower submap:")
        print("(1) Control Center")
        print("(2) Gardens")
        print("(3) Night Market")
        print("(4) Back.")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                if mode == 1:
                    Replay.lijiang_controlcenter()
                elif mode == 2:
                    Live.lijiang_controlcenter()
            elif option == 2:
                if mode == 1:
                    Replay.lijiang_gardens()
                elif mode == 2:
                    Live.lijiang_gardens()
            elif option == 3:
                if mode == 1:
                    Replay.lijiang_nightmarket()
                elif mode == 2:
                    Live.lijiang_nightmarket()
            elif option == 4:
                print("back to control map.")
                return
    return

def select_nepal_submap():
    while True:
        print("Select Nepal submap:")
        print("(1) Sanctum")
        print("(2) Shrine")
        print("(3) Village")
        print("(4) Back.")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            print(mode)
            if option == 1:
                print("Sanctum.")
                if mode == 1:
                    Replay.nepal_sanctum()
                elif mode == 2:
                    Live.nepal_sanctum()
            elif option == 2:
                print("Shrine.")
                if mode == 1:
                    Replay.nepal_shrine()
                elif mode == 2:
                    Live.nepal_shrine()
            elif option == 3:
                print("Village.")
                if mode == 1:
                    Replay.nepal_village()
                elif mode == 2:
                    Live.nepal_village()
            elif option == 4:
                print("back to control map.")
                return
    return

def select_oasis_submap():
    while True:
        print("Select Oasis submap:")
        print("(1) City Center")
        print("(2) Gardens")
        print("(3) University")
        print("(4) Back.")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                if mode == 1:
                    Replay.oasis_citycenter()
                elif mode == 2:
                    Live.oasis_citycenter()
            elif option == 2:
                if mode == 1:
                    Replay.oasis_gardens()
                elif mode == 2:
                    Live.oasis_gardens()
            elif option == 3:
                if mode == 1:
                    Replay.oasis_university()
                elif mode == 2:
                    Live.oasis_university()
            elif option == 4:
                print("back to control map.")
                return
    return

def select_samoa_submap():
    while True:
        print("Select Samoa submap:")
        print("(1) Beach")
        print("(2) Downtown")
        print("(3) Volcano")
        print("(4) Back.")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                if mode == 1:
                    Replay.samoa_beach()
                elif mode == 2:
                    Live.samoa_beach()
            elif option == 2:
                if mode == 1:
                    Replay.samoa_downtown()
                elif mode == 2:
                    Live.samoa_downtown()
            elif option == 3:
                if mode == 1:
                    Replay.samoa_volcano()
                elif mode == 2:
                    Live.samoa_volcano()
            elif option == 4:
                print("back to control map.")
                return
    return

# -----------------------------------------------------------------------------
def select_escort_map():
    return

# -----------------------------------------------------------------------------
def select_flashpoint_map():
    return

# -----------------------------------------------------------------------------
def select_hybrid_map():
    return

# -----------------------------------------------------------------------------
def select_push_map():
    while True:
        print("Select control map:")
        print("(1) Colosseo")
        print("(2) Esperanca")
        print("(3) New Queens Street")
        print("(4) Back")
        option = input("")
        if option in ['1', '2', '3', '4']:
            option = int(option)
            print("You selected ", end="")
            if option == 1:
                print("Colosseo.")
                if mode == 1:
                    Replay.colosseo()
                elif mode == 2:
                    Live.colosseo()
            elif option == 2:
                print("Esperanca.")
                if mode == 1:
                    Replay.esperanca()
                elif mode == 2:
                    Live.esperanca()
            elif option == 3:
                print("New Queens Street.")
                if mode == 1:
                    Replay.newqueensstreet()
                elif mode == 2:
                    Live.newqueensstreet()
            elif option == 4:
                print("Back")
                return
        else:
            print("Invalid input.")
    return


# main function
def main():
    global mode 
    mode = select_mode()
    select_map_type()

# Default notation
if __name__ == "__main__":
    main()


'''00
# when replay code
def replay():
    pyautogui.press("0")

    pyautogui.click()
    pyautogui.keyDown("shift")
    pyautogui.keyDown("e")
    time.sleep(2)
    pyautogui.keyUp("e")
    pyautogui.keyUp("shift")
    
    #pyautogui.dragTo(0, -100)
    pydirectinput.moveTo(0, 40)


# when live lobby
def live():
    pyautogui.press("0")
    pyautogui.press("0")

    pyautogui.click()E
    pyautogui.keyDown("shift")
    pyautogui.keyDown("e")
    time.sleep(2)
    pyautogui.keyUp("e")
    pyautogui.keyUp("shift")
    
    #pyautogui.dragTo(0, -100)
    pydirectinput.moveTo(0, 40)

mode = 2

# find overwatch window
window = pyautogui.getWindowsWithTitle("Overwatch")[0]
if(window):
    # bring window to front
    window.minimize()
    window.maximize()
    
    # determine if mode is live scrim or code
    # we start with replay codes
    # check if game is unpaused or paused
    game_paused = False
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

    # when cart reaches some point, reposition around objective
    
    if mode == 1:
        while True:
            replay()
            time.sleep(15)
    elif mode == 2:
        while True:
            live()
            time.sleep(15)
    
else:
    print("Overwatch not found.")
'''