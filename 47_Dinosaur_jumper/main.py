#region IMPORT

import pyautogui
from selenium import webdriver

#endregion

#region INIT 

#Initializing constants
DINOSAUR_GAME_URL = "https://elgoog.im/t-rex/"
JUMP_PIXEL_VALUE = (83, 83, 83)
RESTART_BUTTON_COR = (956, 429)
XCOR_1 = 758
XCOR_2 = 777
YCOR = 450
JUMP_COUNT = 0

#Initalizing driver
chrome_driver_path = "YOUR CHROME DRIVER PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(DINOSAUR_GAME_URL)

#Initializing gameconditions
screenWidth, screenHeight = pyautogui.size()
pyautogui.getWindowsWithTitle("Play T-Rex Dinosaur Game Online - Google")[0].maximize()
pyautogui.click(RESTART_BUTTON_COR)
pyautogui.press('space')
game_on = True

#endregion

#region MAIN

while game_on:

    #im = pyautogui.screenshot()
    px1 = im.getpixel((XCOR_1, YCOR))
    px2 = im.getpixel((XCOR_2, YCOR))
    px3 = im.getpixel((XCOR_1 + 1, YCOR))

    #Check if any of the pixels indicate an obstacle
    if px1 == JUMP_PIXEL_VALUE or px2 == JUMP_PIXEL_VALUE or px3 == JUMP_PIXEL_VALUE:
        pyautogui.press('space')
        pyautogui.hotkey('ctrl', 'home')
        JUMP_COUNT += 1

        #Adjust XCOR_2 after a certain number of jumps to adapt to game progression
        if JUMP_COUNT == 8:
            XCOR_2 += 5
            JUMP_COUNT = 0

#endregion
