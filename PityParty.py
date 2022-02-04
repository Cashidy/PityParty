import pyautogui
import time

def findPlayButton():
    button = pyautogui.locateOnScreen('pics/play0.png', grayscale = False, confidence = 0.95)
    if button: return button
    else: return pyautogui.locateOnScreen('pics/play1.png', grayscale = False, confidence = 0.95)

playButton = findPlayButton()
while True:
    while playButton:
        pyautogui.moveTo(playButton)
        pyautogui.click()
        pyautogui.move(30, 0)
        time.sleep(230)
        playButton = findPlayButton()
        
    chromeButton = pyautogui.locateOnScreen('pics/chromeTB.png', grayscale = False, confidence = 0.95)
    pyautogui.moveTo(chromeButton)
    pyautogui.click()
    time.sleep(3)
    playButton = findPlayButton()
    if playButton:
        continue

    newTab = pyautogui.locateOnScreen('pics/newTab.png', grayscale = False, confidence = 0.95)
    pyautogui.moveTo(newTab)
    pyautogui.click()
    time.sleep(1)
    pyautogui.write("https://open.spotify.com/album/2v6917Li4tBWEwqtppdlLM\n")
    time.sleep(3)
    playButton = findPlayButton()
