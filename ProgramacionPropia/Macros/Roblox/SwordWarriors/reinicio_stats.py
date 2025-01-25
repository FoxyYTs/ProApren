import threading
import time
import pyautogui
import pynput as pt

pyautogui.FAILSAFE = False

cdq = 1  # Cooldown de la habilidad Q
cde = 6  # Cooldown de la habilidad E
cdf = 28  # Cooldown de la habilidad F

hp = [-24, -652]  # Posición de la barra de HP
attack = [-15, -566]  # Posición de la barra de ataque
reset = [-127, -268]  # Posición del botón de reinicio

x = 5
y = -5

tecla1 = 0  # Estado de la habilidad Q (0: desactivada, 1: activada)
tecla2 = 0  # Estado de la habilidad E
tecla3 = 0  # Estado de la habilidad F

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
    while tecla1:
        pyautogui.keyDown('q')
        countdown(cd)

def habilidadE(cd):
    """Ejecuta la habilidad E con el cooldown especificado."""
    while tecla2 == 1:
        pyautogui.keyDown('e')
        countdown(cd)

def habilidadF(cd):
    """Ejecuta la habilidad F con el cooldown especificado."""
    while tecla3 == 1:
        pyautogui.keyDown('f')
        pyautogui.keyUp('f')
        countdown(cd)

def resetStats():
    """Restablece las estadísticas del personaje."""
    pyautogui.getWindowsWithTitle("Roblox")[0].activate()
    pyautogui.moveTo(hp[0], hp[1], duration=1)
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(attack[0], attack[1], 1)
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(reset[0], reset[1], 1)
    pyautogui.leftClick()
    time.sleep(0.5)

def on_press(key):
    """Maneja las pulsaciones de teclas."""
    global tecla1, tecla2, tecla3
    if key == pt.keyboard.Key.esc:  # Cambiar a num_lock para detectar la tecla Num Lock
        return False
    elif key == pt.keyboard.Key.end:
        tecla1 = not tecla1  # Alternar el estado de la habilidad Q
        if tecla1:
            q.start()
            print("Habilidad Q activada")
        else:
            q.join()
            print("Habilidad Q desactivada")
    
        print('Presionaste la tecla fin', tecla1)
    # ... (Agregar manejo de otras teclas si es necesario)

def detector():
    """Escucha las pulsaciones de teclas."""
    with pt.keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    q = threading.Thread(target=habilidadQ, args=(cdq,))
    e = threading.Thread(target=habilidadE, args=(cde,))
    f = threading.Thread(target=habilidadF, args=(cdf,))

    try:
        while True:
            detector() 
    except KeyboardInterrupt:
        print("Programa detenido por el usuario.")