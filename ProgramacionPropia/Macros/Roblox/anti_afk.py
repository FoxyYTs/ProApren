import time
import pyautogui
pyautogui.FAILSAFE = False

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

    print('¡Tiempo cumplido!')

def move():
    # Presionar A y mantenerla por 5 segundos
    pyautogui.keyDown('a')
    time.sleep(0.5)
    pyautogui.keyUp('a')

    # Presionar B y mantenerla por 5 segundos
    pyautogui.keyDown('d')
    time.sleep(0.5)
    pyautogui.keyUp('d')

while True:
    countdown(15)
    move()