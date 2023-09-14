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
    print(terminate_thread)
    while not terminate_thread:
        while(True):
            getScreen(path)
            sleep(seconds)
    else: print("exit")