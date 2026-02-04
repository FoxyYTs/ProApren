import qrcode
import os
from datetime import datetime

def generar_qr(enlace, nombre_archivo=None, directorio="codigos_qr"):
    """
    Genera un código QR a partir de un enlace web
    
    Args:
        enlace (str): URL o texto para convertir en QR
        nombre_archivo (str): Nombre del archivo (opcional)
        directorio (str): Directorio donde guardar el QR
    """
    
    # Crear directorio si no existe
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    
    # Generar nombre de archivo si no se proporciona
    if not nombre_archivo:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nombre_archivo = f"qr_{timestamp}.png"
    
    # Configuración del QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Añadir datos y generar QR
    qr.add_data(enlace)
    qr.make(fit=True)
    
    # Crear y guardar imagen
    img = qr.make_image(fill_color="black", back_color="white")
    ruta_completa = os.path.join(directorio, nombre_archivo)
    img.save(ruta_completa)
    
    print(f"✅ Código QR generado exitosamente!")
    print(f"📁 Guardado en: {ruta_completa}")
    print(f"🔗 Enlace: {enlace}")
    
    return ruta_completa

# Ejemplo de uso
if __name__ == "__main__":
    # El enlace que quieres convertir
    enlace_web = "https://docs.google.com/document/u/1/d/1D7TtgA0Ky274nMDGHmMpWgyNzXfVWeVX/mobilebasic?pli=1"
    
    # Generar el QR
    generar_qr(enlace_web, "mi_documento_qr.png")