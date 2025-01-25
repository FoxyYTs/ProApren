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

def ejecutar_aplicacion_y_cerrar():
    # Iniciar la aplicación (reemplaza 'ruta_a_la_aplicacion.exe' con la ruta correcta)
    pyautogui.hotkey('win', 'r')
    time.sleep(1)
    pyautogui.typewrite('steam://rungameid/2923300')
    pyautogui.press('enter')

    # Esperar unos segundos para que la aplicación se cargue (ajusta según sea necesario)
    time.sleep(10)

    # Obtener las dimensiones de la pantalla
    screen_width, screen_height = pyautogui.size()

    # Hacer clic en el centro de la pantalla
    print("pulsar")
    pyautogui.click(screen_width/2, screen_height/2)
    pyautogui.click(screen_width/2, screen_height/2)
    pyautogui.click(screen_width/2, screen_height/2)

    # Esperar unos segundos más
    time.sleep(2)

    # Cerrar la aplicación (puede requerir diferentes comandos según la aplicación)
    pyautogui.hotkey('alt', 'f4')

while True:
    ejecutar_aplicacion_y_cerrar()
    countdown(11400)