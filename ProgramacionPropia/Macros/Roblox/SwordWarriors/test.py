import time

import pyautogui


def countdown(t):
    """Cuenta atrás desde un tiempo dado."""
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('¡Tiempo cumplido!')

def habilidadQ(cd):
    """Ejecuta la habilidad Q con el cooldown especificado."""
    print("Ejecutando habilidad Q...")
    while True:
        pyautogui.keyDown('e')
        countdown(cd)

countdown(5)
habilidadQ(5)