from Vehiculo import Vehiculo
import openpyxl
import pandas as pd
datos=["Id","Nombre","Anio","Marca","Tipo","Combustible","Precio","NumeroPuertas","Descapotable","NumeroLlantas","TipoAutomovil","Propulsion"]
datosExcel=["id","nombre","anio","marca","tipo","combustible","precio","numeroPuertas","descapotable","numeroLlantas","tipoAutomovil","propulsion"]

class Automovil(Vehiculo):
    def __init__(self, id=""):
        self.hojaAutomovil = pd.read_excel("Entregable2/resources/Clases.xlsx","ClaseAutomovil",index_col="placa")
        self.hojaVehiculo = pd.read_excel("Entregable2/resources/Clases.xlsx","ClaseVehiculo",index_col="id")
        """Automovil
            id (String): Identificacion del vehiculo (Ej: Una Placa)
            nombre (String): Nombre del modelo del vehiculo
            anio (int): Anio de lanzamiento
            marca (String): Fabricante del vehiculo
            tipo (String): Tipo de vehiculo (Ej: Carro, moto, bote, avioneta, etc...)
            combustible (String): Combustible del vehiculo
            precio (double): Precio del Vehiculo
            numeroPuertas (int): cantidad de puertas del automovil
            descapotable (boolean): ¿Es descapotable?
            numeroLlantas (int): Cantidad de llantas del automovil
            tipoAutomovil (String): tipo del vehiculo (ej: Hatchback,deportivo,pickup, sedan, etc...)
            propulsion (String): tipo de propulsion del vehiculo (ej: trasera, delantera, total)

        Args:
            id (String) =  Identificacion del vehiculo (ej: una placa)
        """
        super().__init__(id, self.hojaVehiculo.loc[id, "nombre"], int(self.hojaVehiculo.loc[id, "anio"]), self.hojaVehiculo.loc[id, "marca"], self.hojaVehiculo.loc[id, "tipo"],self.hojaVehiculo.loc[id, "combustible"],float(self.hojaVehiculo.loc[id, "precio"]))
        self.placa = id
        self.numeroPuertas = int(self.hojaAutomovil.loc[id, "numeroPuertas"])
        self.descapotable = bool(self.hojaAutomovil.loc[id, "descapotable"])
        self.numeroLlantas = int(self.hojaAutomovil.loc[id, "numeroLlantas"])
        self.tipoAutomovil = self.hojaAutomovil.loc[id, "tipoAutomovil"]
        self.propulsion = self.hojaAutomovil.loc[id, "propulsion"]
        
    def IniciarTabla(self):
        """
            Creación de las tablas con respectiva columnas
        """
        self.CrearTabla("Vehiculo", "ColumnasVehiculo")
        self.CrearTabla("Automovil","ColumnasAutomovil")

    def agregarDatos(self):
        """
            Inserta los datos a la base de datos ya creada
        """
        datosV = [
            (self.id,self.nombre, self.anio, self.marca, self.tipo, self.combustible, self.precio)
        ]
        self.InsertarDato("Vehiculo","?,?,?,?,?,?,?",datosV)
        datosA = [
            (self.id,self.numeroPuertas,self.descapotable,self.numeroLlantas,self.tipoAutomovil,self.propulsion)
        ]
        self.InsertarDato("Automovil","?,?,?,?,?,?",datosA)
        print("Datos Agregados.")
    
    def EliminarDatos(self):
        """
            Elimina los datos dependiendo de su clave primaria o foranea
        """
        self.EliminarDato("Vehiculo", self.id)
        self.EliminarDato("Automovil", self.placa)
        print("Datos eliminados.")
    
    def LeerDatos(self):
        """
            Muestra los registros de la base de datos
        """
        print("============================")
        datosV = self.LeerDato("Vehiculo", self.id)
        print(f"1. ID/Placa: {datosV[0]}\n2. Nombre: {datosV[1]}\n3. Anio: {datosV[2]}\n4. Marca: {datosV[3]}\n5. Tipo: {datosV[4]}\n6. Combustible: {datosV[5]}\n7. Precio: {datosV[6]}")
        datosA = self.LeerDato("Automovil", self.placa)
        print(f"8. Numero de Puertas: {datosA[1]}\n9. Es descapotable: {datosA[2]}\n10. NumeroLlantas: {datosA[3]}\n11. Tipo de Automovil: {datosA[4]}\n12. Propulsion: {datosA[5]}")
        print("============================")
                
    def ActualizarDatos(self, datoAct,datoCambio):
        """
            Actualiza los datos usando el numero de dato a cambiar y el dato dependiendo de su tipo.
        """
        if datoAct-1 == 1:
            self.ActualizarDato("Vehiculo", datos[datoAct-1], datoCambio, self.id)
            self.ActualizarDato("Automovil", datos[datoAct-1], datoCambio, self.id)
        elif datoAct-1 == 2 or datoAct-1 == 4 or datoAct-1 == 5 or datoAct-1 == 6:
            self.ActualizarDato("Vehiculo", datos[datoAct-1], datoCambio, self.id)
        elif datoAct-1 == 3:
            self.ActualizarDato("Vehiculo", datos[datoAct-1], int(datoCambio), self.id)
        elif datoAct-1 == 7:
            self.ActualizarDato("Vehiculo", datos[datoAct-1], float(datoCambio), self.id)
        elif datoAct-1 == 8 or datoAct-1 == 10:
            self.ActualizarDato("Automovil", datos[datoAct-1], int(datoCambio), self.id)
        elif datoAct-1 == 9:
            self.ActualizarDato("Automovil", datos[datoAct-1], bool(datoCambio), self.id)
        elif datoAct-1 == 11 or datoAct-1 == 12:
            self.ActualizarDato("Automovil", datos[datoAct-1], datoCambio, self.id)
        print("Datos actualizados.")
        
        # GETTERS
    def getPlaca(self):
        """Retorna la placa del automóvil."""
        return self.placa

    def getNumeroPuertas(self):
        """Retorna el número de puertas del automóvil."""
        return self.numeroPuertas

    def getDescapotable(self):
        """Retorna `True` si el automóvil es descapotable, `False` en caso contrario."""
        return self.descapotable

    def getNumeroLlantas(self):
        """Retorna el número de llantas del automóvil."""
        return self.numeroLlantas

    def getTipoAutomovil(self):
        """Retorna el tipo de automóvil (por ejemplo, sedán, SUV, etc.)."""
        return self.tipoAutomovil

    def getPropulsion(self):
        """Retorna el tipo de propulsión del automóvil (por ejemplo, trasera, delantera, total)."""
        return self.propulsion

    # SETTERS
    def setPlaca(self, placa):
        """Establece la placa del automóvil.

        Args:
            placa(String): Identificacion del vehiculo
        """
        self.placa = placa

    def setNumeroPuertas(self, numeroPuertas):
        """Establece el número de puertas del automóvil.

        Args:
            numeroPuertas(int): Cantidad de puertas del automovil
        """
        self.numeroPuertas = numeroPuertas

    def setDescapotable(self, descapotable):
        """Establece si el automóvil es descapotable o no.

        Args:
            descapotable(boolean): ¿Es descapotable?
        """
        self.descapotable = descapotable

    def setNumeroLlantas(self, numeroLlantas):
        """Establece el número de llantas del automóvil.

        Args:
            numeroLlantas(int): Cantidad de llantas del automovil
        """
        self.numeroLlantas = numeroLlantas

    def setTipoAutomovil(self, tipoAutomovil):
        """Establece el tipo de automóvil (por ejemplo, sedán, SUV, etc.).

        Args:
            tipoAutomovil(String): Tipo del vehiculo (ej: Hatchback,deportivo,pickup, sedan, etc...)
        """
        self.tipoAutomovil = tipoAutomovil

    def setPropulsion(self, propulsion):
        """Establece el tipo de propulsión del automóvil (por ejemplo, trasera, delantera, total).

        Args:
            propulsion(String): Tipo de propulsion del vehiculo (ej: trasera, delantera, total)
        """
        self.propulsion = propulsion