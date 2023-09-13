from datetime import datetime
import pyautogui

def main():
    getScreen("./")
    
def getScreen(savePath : str):
        screen = pyautogui.screenshot()
        screen.save(fr'{savePath}\{getFileName()}.png')
        
def getFileName():
    time = datetime.now() 
    return f'Screenshot {time.strftime("%d-%m-%Y %H-%M-%S")}';

if __name__ == "__main__":
    main()