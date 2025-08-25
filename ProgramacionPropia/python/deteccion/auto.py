import pyautogui
import pygetwindow as gw
import time

# Nombre del archivo de imagen del botón
nombre_del_boton = 'ProgramacionPropia/python/deteccion/boton1.png'

# Encuentra la ventana de la aplicación por su título
try:
    ventana_app = gw.getWindowsWithTitle('Roblox')[0]
    
    # Activa la ventana para asegurar que esté visible en la pantalla
    print(f"Activando la ventana '{ventana_app.title}'...")
    ventana_app.activate()
    time.sleep(2)  # Pausa para dar tiempo a que la ventana se active

    # Vuelve a obtener las coordenadas de la ventana después de activarla
    # Esto asegura que las coordenadas sean válidas
    region_de_busqueda = (ventana_app.left, ventana_app.top, ventana_app.width, ventana_app.height)
    
    print(f"Buscando el botón '{nombre_del_boton}' solo en la ventana: {region_de_busqueda}")
except IndexError:
    print("La ventana especificada no se encontró. Asegúrate de que la aplicación esté abierta y el título sea correcto.")
    exit()

# Bucle de detección
while True:
    try:
        ubicacion = pyautogui.locateOnScreen(nombre_del_boton, confidence=0.8, region=region_de_busqueda)
        
        if ubicacion:
            print(f"✅ ¡Éxito! El botón '{nombre_del_boton}' ha sido detectado dentro de la ventana.")
            # Opcional: pyautogui.click(ubicacion)
            break
        else:
            print("El botón no ha sido encontrado. Reintentando en 1 segundo...")
            time.sleep(1)

    except pyautogui.ImageNotFoundException:
        print("El botón no ha sido encontrado. Reintentando en 1 segundo...")
        time.sleep(1)