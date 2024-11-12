class Puente:
    def __init__(self, tipo_material, longitud, ancho, altura, costo_por_metro_cubico):
        self.tipo_material = tipo_material
        self.longitud = longitud
        self.ancho = ancho
        self.altura = altura
        self.costo_por_metro_cubico = costo_por_metro_cubico

    def cal_volumen(self):
        return self.longitud * self.ancho * self.altura

    def cal_costo_mat(self):
        volumen = self.cal_volumen()
        return volumen * self.costo_por_metro_cubico

    def aplicar_descuento(self, costo_total):
        if costo_total >= 2000000 and costo_total < 40000000:
            descuento = costo_total * 0.1
        elif costo_total >= 40000000:
            descuento = costo_total * 0.2
        else:
            descuento = 0
        return costo_total - descuento

def solicitar_datos_puente():
    tipo_material = input("Ingrese el tipo de material (ej: concreto, acero): ")
    longitud = float(input("Ingrese la longitud del puente en metros: "))
    ancho = float(input("Ingrese el ancho del puente en metros: "))
    altura = float(input("Ingrese la altura del puente en metros: "))
    costo_por_metro_cubico = float(input("Ingrese el costo por metro cúbico del material: "))
    return Puente(tipo_material, longitud, ancho, altura, costo_por_metro_cubico)

def cal_y_mostrar_costo(puente, nombre_usuario):
    costo_materiales = puente.cal_costo_materiales()
    iva = costo_materiales * 0.19  # Suponiendo un IVA del 19%
    costo_total = costo_materiales + iva
    costo_final = puente.aplicar_descuento(costo_total)

    print("\nCotización para", nombre_usuario)
    print("Tipo de material:", puente.tipo_material)
    print("Costo total de los materiales (sin IVA):", costo_materiales)
    print("IVA:", iva)
    print("Costo total antes de descuento:", costo_total)
    print("Descuento aplicado:", costo_total - costo_final)
    print("Costo final:", costo_final)

if __name__ == "__main__":
    while True:
        nombre_usuario = input("Ingrese su nombre (o escriba 'salir' para terminar): ")
        if nombre_usuario.lower() == "salir":
            break

        puente = solicitar_datos_puente()
        cal_y_mostrar_costo(puente, nombre_usuario)