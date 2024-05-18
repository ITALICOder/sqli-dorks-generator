import pyautogui
import time
import keyboard
def move_and_click(x, y):
    pyautogui.moveTo(x, y)
    #time.sleep(1)
    pyautogui.click()
def cento_stringe(file):
    with open(file, 'r') as f:
        lines = [next(f) for x in range(100)]
    with open(file, 'r+') as f:
        data = f.readlines()
        f.seek(0)
        f.truncate()
        f.writelines(data[100:])
    return lines

if __name__ == "__main__":
    while keyboard.is_pressed('q') == False:
        if pyautogui.locateOnScreen('dumping_finished.png', confidence=0.9) is not None:
            #click queue add cento_stringe and start the url searching
            x, y = pyautogui.locateCenterOnScreen('queue.png', confidence=0.95)
            move_and_click(x, y)
            time.sleep(1)
            move_and_click(1764, 170)
            time.sleep(1)
            pyautogui.hotkey('ctrl', 'a')
            time.sleep(1)
            for line in cento_stringe('dorks.txt'):
                pyautogui.typewrite(line)
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('start.png', confidence=0.7)
            move_and_click(x, y)
            print("Dumper_finished count")
        if pyautogui.locateOnScreen('scan_finished.png', confidence=0.9) is not None:
            #click sqli injection, click start
            x, y = pyautogui.locateCenterOnScreen('sqli.png', confidence=0.9)
            move_and_click(x, y)
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('start_exp.png', confidence=0.9)
            move_and_click(x, y)
            print("Scan_finished count")
        if pyautogui.locateOnScreen('work_cancel.png', confidence=0.9) is not None:
            x, y = pyautogui.locateCenterOnScreen('queue.png', confidence=0.9)
            move_and_click(x, y)
            time.sleep(1)
            x, y = pyautogui.locateCenterOnScreen('start.png', confidence=0.7)
            move_and_click(x, y)
            print("Canceled_finished count")
