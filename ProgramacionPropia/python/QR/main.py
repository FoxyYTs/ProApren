import qrcode

# El enlace que quieres convertir en un código QR
enlace_web = "https://forms.gle/BBx6Lz7rqEkWkjjG6"  # Puedes cambiar este enlace por el que desees

# Crear un objeto de código QR
# version: 1 a 40 (determina el tamaño del QR, a mayor número, más grande y más datos puede almacenar)
# error_correction: Nivel de corrección de errores (L, M, Q, H)
# box_size: Tamaño de cada "caja" o píxel del código QR
# border: Grosor del borde blanco alrededor del código
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Añadir los datos (el enlace) al objeto QR
qr.add_data(enlace_web)
qr.make(fit=True)

# Crear la imagen del código QR
# fill_color: Color de los cuadrados del QR
# back_color: Color del fondo
img = qr.make_image(fill_color="black", back_color="white")

# Guardar la imagen en un archivo
nombre_archivo = "mi_qr.png"
img.save(nombre_archivo)

print(f"Código QR guardado como '{nombre_archivo}'")