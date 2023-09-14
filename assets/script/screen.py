from datetime import datetime
from time import sleep
import pyautogui

terminate_thread = False

def getScreen(savePath : str):
    screen = pyautogui.screenshot()
    screen.save(fr'{savePath}\{getFileName()}.png')
        
def getFileName():
    time = datetime.now() 
    return f'Screenshot {time.strftime("%d-%m-%Y %H-%M-%S")}';

def run(seconds : int, path : str):
    while not terminate_thread:
        print(terminate_thread)
        getScreen(path)
        sleep(seconds)