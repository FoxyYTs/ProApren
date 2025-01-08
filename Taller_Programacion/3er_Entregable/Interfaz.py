import tkinter as tk
from tkinter import messagebox, ttk
from Zoos import Zoo
from Animals import Animal
class Interfaz:
    def __init__(self):
        """
        Inicializa la instancia de la clase.
        """
        self.zoo = Zoo()
        self.animal = Animal()
        self.ventana = tk.Tk()
        self.ventana.title("Base de Datos del Zoologico")
        self.ventana.geometry("1200x450")

        
        self.nb = ttk.Notebook(self.ventana)
        self.nb.pack(fill = "both", expand = "yes")

        # Menu Zoologico
        self.ZooMenu = tk.Frame(self.ventana)
        self.ZooMenu.config(bg="#242424")

        self.zooEncabezado = tk.Frame(self.ZooMenu)
        self.zooEncabezado.grid(row=0, column=0)

        self.zooTitulo = tk.Label(self.zooEncabezado, text = "ZOOLOGICO")
        self.zooTitulo.config(font = ("Comic Sans MS", 20), foreground = "#428C00", bg="#242424")
        self.zooTitulo.grid(row = 0, column = 0)

        self.zooInfoMenu = tk.Frame(self.ZooMenu)
        self.zooInfoMenu.config(bg="#242424")
        self.zooInfoMenu.grid(row = 1, column = 0)
        self.zooCampo()

        self.zooModMenu = tk.Frame(self.ZooMenu)
        self.zooModMenu.config(bg="#242424")
        self.zooModMenu.grid(row = 2, column = 0)
        self.zooMod()

        self.zooTablaMenu = tk.Frame(self.ZooMenu)
        self.zooTablaMenu.grid(row = 1, column = 1)
        self.zooTabla()
        self.zooCargar()


        

        # Menu Animales
        self.AnimalMenu = tk.Frame(self.ventana)
        self.AnimalMenu.config(bg="#242424")

        self.animalEncabezado = tk.Frame(self.AnimalMenu)
        self.animalEncabezado.grid(row=0, column=0)

        self.animalTitulo = tk.Label(self.animalEncabezado, text = "ANIMALES")
        self.animalTitulo.config(font = ("Comic Sans MS", 20), foreground = "#428C00", bg="#242424")
        self.animalTitulo.grid(row = 0, column = 0)

        self.animalInfoMenu = tk.Frame(self.AnimalMenu)
        self.animalInfoMenu.config(bg="#242424")
        self.animalInfoMenu.grid(row = 1, column = 0, padx = 5, pady = 10)
        self.animalCampo()

        self.animalModMenu = tk.Frame(self.AnimalMenu)
        self.animalModMenu.config(bg="#242424")
        self.animalModMenu.grid(row = 2, column = 0)
        self.animalMod()

        self.animalTablaMenu = tk.Frame(self.AnimalMenu)
        self.animalTablaMenu.config(bg="#242424")
        self.animalTablaMenu.grid(row = 1, column = 1, padx = 10, pady = 10)
        self.animalTabla()
        self.animalCargar()


        # Cargar Interfaz
        self.center_window()
        self.nb.add(self.ZooMenu, text = "ZOOLOGICOS")
        self.nb.add(self.AnimalMenu, text = "ANIMALES")
        self.ventana.mainloop()

    # Centrar pantalla
    def center_window(self):
        """
        Centra la ventana en la pantalla.

        Esta función actualiza las tareas inactivas de la ventana, calcula las coordenadas x e y para centrar la ventana y
        establece la geometría de la ventana en consecuencia.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            Ninguno
        """
        self.ventana.update_idletasks()
        x = (self.ventana.winfo_screenwidth() // 2) - (self.ventana.winfo_width() // 2)
        y = (self.ventana.winfo_screenheight() // 2) - (self.ventana.winfo_height() // 2)
        self.ventana.geometry(f'{self.ventana.winfo_width()}x{self.ventana.winfo_height()}+{x}+{y}')
    # Diseño del Menu Zoo y Funcionalidad
    def zooCampo(self):
        """
        Crea una interfaz gráfica para un campo de zoologíco con etiquetas y campos de entrada para el nombre y la ubicación.
        La función también crea botones para agregar nuevas entradas, guardar entradas y cancelar.
        Esta función no toma ningún parámetro y no devuelve nada.
        """
        self.campoZName = tk.Label(self.zooInfoMenu, text="Nombre: ")
        self.campoZName.config(bg="#242424", fg="#ffffff")
        self.campoZName.grid(row=0, column=0, padx = 5, pady = 5)

        self.varZName = tk.StringVar()
        self.campoZName = tk.Entry(self.zooInfoMenu, textvariable=self.varZName)
        self.campoZName.config(bg="#242424", fg="#ffffff", state = "disabled")
        self.campoZName.grid(row=0, column=1, padx = 5, pady = 5)

        self.campoUbi = tk.Label(self.zooInfoMenu, text="Ubicacion: ")
        self.campoUbi.config(bg="#242424", fg="#ffffff")
        self.campoUbi.grid(row=1, column=0, padx = 5, pady = 5)
        
        self.varUbi = tk.StringVar()
        self.campoUbi = tk.Entry(self.zooInfoMenu, textvariable=self.varUbi)
        self.campoUbi.config(bg="#242424", fg="#ffffff", state = "disabled")
        self.campoUbi.grid(row=1, column=1)

        self.ZNuevo = tk.Button(self.zooInfoMenu, text = "Nuevo", bg = "#428C00", width=10, height=1, command = self.EvZNuevo)
        self.ZNuevo.grid(row = 2, column = 0, padx = 10, pady = 10)

        self.ZGuardar = tk.Button(self.zooInfoMenu, text = "Guardar", bg = "#428C00", width=10, height=1, command = self.EvZGurdar)
        self.ZGuardar.config(state = "disabled")
        self.ZGuardar.grid(row = 2, column = 1, padx = 1, pady = 10)

        self.ZCancelar = tk.Button(self.zooInfoMenu, text = "Cancelar", bg = "#428C00", width=10, height=1, command = self.EvZCancelar)
        self.ZCancelar.config(state = "disabled")
        self.ZCancelar.grid(row = 2, column = 2, padx = 10, pady = 10)

    # Diseño del Menu Animal y Funcionalidad
    def animalCampo(self):
        """
        Crea una GUI para ingresar información de animales. La función inicializa varios etiquetas y campos de entrada 
        para que el usuario pueda ingresar el nombre, especie y ID de un animal en un zoo. También crea botones para guardar 
        y cancelar la entrada. La función no toma parámetros y no devuelve nada.
        """
        self.campoAName = tk.Label(self.animalInfoMenu, text="Nombre: ")
        self.campoAName.config(bg="#242424", fg="#ffffff")
        self.campoAName.grid(row=0, column=0, padx = 5, pady = 5)

        self.varAName = tk.StringVar()
        self.campoAName = tk.Entry(self.animalInfoMenu, textvariable=self.varAName)
        self.campoAName.config(bg="#242424", fg="#ffffff", state = "disabled")
        self.campoAName.grid(row=0, column=1, padx = 5, pady = 5)

        self.campoSpe = tk.Label(self.animalInfoMenu, text="Especie: ")
        self.campoSpe.config(bg="#242424", fg="#ffffff")
        self.campoSpe.grid(row=1, column=0, padx = 5, pady = 5)
        
        self.varSpe = tk.StringVar()
        self.campoSpe = tk.Entry(self.animalInfoMenu, textvariable=self.varSpe)
        self.campoSpe.config(bg="#242424", fg="#ffffff", state = "disabled")
        self.campoSpe.grid(row=1, column=1)

        self.campoID = tk.Label(self.animalInfoMenu, text="Zoo ID: ")
        self.campoID.config(bg="#242424", fg="#ffffff")
        self.campoID.grid(row=2, column=0)

        self.varZooID = tk.IntVar()
        self.campoID = tk.Entry(self.animalInfoMenu, textvariable = self.varZooID)
        self.campoID.config(bg="#242424", fg="#ffffff", state = "disabled")
        self.campoID.grid(row = 2, column = 1, padx = 5, pady = 5)

        self.ANuevo = tk.Button(self.animalInfoMenu, text = "Nuevo", bg = "#428C00", width=10, height=1, command = self.EvANuevo)
        self.ANuevo.grid(row = 3, column = 0, padx = 10, pady = 10)

        self.AGuardar = tk.Button(self.animalInfoMenu, text = "Guardar", bg = "#428C00", width=10, height=1, command = self.EvAGurdar)
        self.AGuardar.config(state = "disabled")
        self.AGuardar.grid(row = 3, column = 1, padx = 1, pady = 10)

        self.ACancelar = tk.Button(self.animalInfoMenu, text = "Cancelar", bg = "#428C00", width=10, height=1, command = self.EvACancelar)
        self.ACancelar.config(state = "disabled")
        self.ACancelar.grid(row = 3, column = 2, padx = 10, pady = 10)

    # Modificar Datos
    def zooMod(self):
        """
        Inicializa los elementos de la GUI para el menu zooMod.

        Esta función crea y configura los etiquetas, campos de entrada y botones para el menu zooMod.
        Las etiquetas y campos de entrada se utilizan para mostrar y ingresar el ID del animal del zoo a modificar.
        Los botones se utilizan para activar los controladores de eventos correspondientes para editar y eliminar el animal del zoo.

        Parámetros:
        - self: La instancia de la clase.

        Retorno:
        - Ninguno
        """
        self.campoZModID = tk.Label(self.zooModMenu, text="ID: ")
        self.campoZModID.config(bg="#242424", fg="#ffffff")
        self.campoZModID.grid(row=0, column=0)

        self.varZModID = tk.IntVar()
        self.campoZModID = tk.Entry(self.zooModMenu, textvariable = self.varZModID)
        self.campoZModID.config(bg="#242424", fg="#ffffff")
        self.campoZModID.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.ZEditar = tk.Button(self.zooModMenu, text = "Editar", bg = "#428C00", width=10, height=1, command = self.EvZEditar)
        self.ZEditar.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.ZEliminar = tk.Button(self.zooModMenu, text = "Eliminar", bg = "#428C00", width=10, height=1, command = self.EvZEliminar)
        self.ZEliminar.grid(row = 1, column = 1, padx = 10, pady = 10)
    def animalMod(self):
        """
        Crea los elementos de la interfaz gráfica para el menú de modificación de animales.

        Esta función inicializa y configura los elementos de etiqueta, campo de entrada y
        botones necesarios para el menú de modificación de animales. Crea una etiqueta
        para el campo de ID, un campo de entrada para el ID y dos botones para editar
        y eliminar un animal.

        Parámetros:
        - self: La instancia de la clase.

        Retorna:
        - Ninguno
        """
        self.campoAModID = tk.Label(self.animalModMenu, text="ID: ")
        self.campoAModID.config(bg="#242424", fg="#ffffff")
        self.campoAModID.grid(row=0, column=0)

        self.varAModID = tk.IntVar()
        self.campoAModID = tk.Entry(self.animalModMenu, textvariable = self.varAModID)
        self.campoAModID.config(bg="#242424", fg="#ffffff")
        self.campoAModID.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.AEditar = tk.Button(self.animalModMenu, text = "Editar", bg = "#428C00", width=10, height=1, command = self.EvAEditar)
        self.AEditar.grid(row = 1, column = 0, padx = 10, pady = 10)

        self.AEliminar = tk.Button(self.animalModMenu, text = "Eliminar", bg = "#428C00", width=10, height=1, command = self.EvAEliminar)
        self.AEliminar.grid(row = 1, column = 1, padx = 10, pady = 10)

    # DB ZOO
    def zooTabla(self):
        """
        Inicializa y configura un widget Treeview para mostrar una tabla de zoológico.

        Parámetros:
            self (objeto): La instancia de la clase.
        
        Retorna:
            Ninguno
        """
        self.tablaZoo = ttk.Treeview(self.zooTablaMenu, show = "headings")
        self.tablaZoo.config(columns = ("ID", "Nombre", "Ubicación"))
        self.tablaZoo.heading("ID", text = "ID")
        self.tablaZoo.heading("Nombre", text = "NOMBRE")
        self.tablaZoo.heading("Ubicación", text = "UBICACION")
        self.tablaZoo.grid(row = 0, column = 0)

        self.zooScroll = tk.Scrollbar(self.zooTablaMenu, command = self.tablaZoo.yview)
        self.zooScroll.grid(row = 0, column = 1, sticky = "ns")
        self.tablaZoo.config(yscrollcommand = self.zooScroll.set)

    # DB ANIMAL
    def animalTabla(self):
        """
        Inicializa y configura un widget Treeview para mostrar datos de animales.

        Parámetros:
            self (object): La instancia de la clase.
        
        Retorna:
            None
        """
        self.tablaAnimal = ttk.Treeview(self.animalTablaMenu, show = "headings")
        self.tablaAnimal.config(columns = ("ID", "Nombre", "Especie", "Zoo_ID"))
        self.tablaAnimal.heading("ID", text = "ID")
        self.tablaAnimal.heading("Nombre", text = "NOMBRE")
        self.tablaAnimal.heading("Especie", text = "ESPECIE")
        self.tablaAnimal.heading("Zoo_ID", text = "ZOO_ID")
        self.tablaAnimal.grid(row = 0, column = 0)

        self.animalScroll = tk.Scrollbar(self.animalTablaMenu, command = self.tablaAnimal.yview)
        self.animalScroll.grid(row = 0, column = 1, sticky = "ns")
        self.tablaAnimal.config(yscrollcommand = self.animalScroll.set)

    # Carga La Base de Datos en Interfaz
    def animalCargar(self):
        """
        Carga los datos del animal en la tabla de la GUI.

        Esta función lee los datos del animal desde el objeto `animal` y los muestra en la tabla de la GUI. 
        Primero borra los datos existentes en la tabla y luego itera sobre cada fila en el atributo `datosEnLaTabla` 
        del objeto `animal`. Para cada fila, inserta los valores en la tabla utilizando el método `insert` del widget `tablaAnimal`.

        Si ocurre un error al leer los datos del animal, se muestra un cuadro de diálogo de advertencia con el mensaje "No se pudo leer la tabla".

        No devuelve nada.
        """
        try:
            self.animal.leer()
            self.tablaAnimal.delete(*self.tablaAnimal.get_children())
            for fila in self.animal.datosEnLaTabla:
                self.tablaAnimal.insert("","end",values=fila)
        except:
            messagebox.showwarning("Error", "No se pudo leer la tabla")

    def zooCargar(self):
        """
        Carga los datos del zoo en la tablaZoo.

        Esta función lee los datos del zoo y los carga en la tablaZoo en la interfaz gráfica.
        Primero, elimina cualquier dato existente en la tablaZoo. Luego, itera sobre los datos del zoo
        y los inserta en cada fila de la tablaZoo. Si ocurre un error durante el proceso de carga,
        se muestra un mensaje de advertencia.

        Parámetros:
            self (objeto): La instancia de la clase.

        Retorna:
            Ninguno
        """
        try:
            self.zoo.leer()
            self.tablaZoo.delete(*self.tablaZoo.get_children())
            for fila in self.zoo.datosEnLaTabla:
                self.tablaZoo.insert("","end",values=fila)
        except:
            messagebox.showwarning("Error", "No se pudo leer la tabla")
    # EVENTLISTENER BOTONES ZOO Y ANIMAL
    def EvZNuevo(self):
        """
        Inicializa los atributos de la clase Zoo con sus valores predeterminados y configura los elementos de la GUI para agregar un nuevo zoo.

        Parámetros:
        self (Zoo): La instancia de la clase Zoo.

        Retorna:
        Ninguno
        """
        self.varZName.set("")
        self.varUbi.set("")
        self.campoZName.config(state = "normal")
        self.campoUbi.config(state = "normal")
        self.ZGuardar.config(state = "normal")
        self.ZCancelar.config(state = "normal")
    
    def EvANuevo(self):
        """
        Inicializa los atributos de la clase Animal con sus valores predeterminados y configura los elementos de la GUI para agregar un nuevo Animal.

        Parámetros:
        self (Animal): La instancia de la clase Animal.

        Retorna:
        Ninguno
        """
        self.varAName.set("")
        self.varSpe.set("")
        self.varZooID.set(0)
        self.campoAName.config(state= "normal")
        self.campoSpe.config(state = "normal")
        self.campoID.config(state = "normal")
        self.AGuardar.config(state = "normal")
        self.ACancelar.config(state = "normal")

    def EvZGurdar(self):
        """
        Función para guardar la información del zoo en la base de datos y mostrarla.

        Parámetros:
        - self: La instancia de la clase.

        Retorno:
        - Ninguno
        """
        if self.varZName.get() and self.varUbi.get():
            self.zoo.nombre = self.varZName.get()
            self.zoo.ubicacion = self.varUbi.get()
            self.zoo.insertar()
            self.zooCargar()
            self.EvZCancelar()
        else:
            messagebox.showwarning("Alerta", "Debes rellenar todos los campos")

    def EvAGurdar(self):
        """
        Función para guardar la información del zoo en la base de datos y mostrarla.

        Parámetros:
        - self: La instancia de la clase.

        Retorno:
        - Ninguno
        """
        if self.varAName.get() and self.varSpe.get() and self.varZooID:
            self.animal.nombre = self.varAName.get()
            self.animal.especie = self.varSpe.get()
            self.animal.zooID = self.varZooID.get()
            self.animal.insertar()
            self.animalCargar()
            self.EvACancelar()
        else:
            messagebox.showwarning("Alerta", "Debes rellenar todos los campos")

    def EvZCancelar(self):
        """
        Establece los valores de `varZName` y `varUbi` como cadenas vacías, deshabilita los campos `campoZName`
        y `campoUbi`, y deshabilita los botones `ZGuardar` y `ZCancelar`.
        """
        self.varZName.set("")
        self.varUbi.set("")
        self.campoZName.config(state = "disabled")
        self.campoUbi.config(state = "disabled")
        self.ZGuardar.config(state = "disabled")
        self.ZCancelar.config(state = "disabled")

    def EvACancelar(self):
        """
        Establece los valores de `varAName`, `varSpe` y `varZooID` como cadenas vacías, deshabilita los campos `campoZName`
        , `campoSpe` y `campoID`, y deshabilita los botones `AGuardar` y `ACancelar`.
        """
        self.varAName.set("")
        self.varSpe.set("")
        self.varZooID.set(0)
        self.campoAName.config(state = "disabled")
        self.campoSpe.config(state = "disabled")
        self.campoID.config(state = "disabled")
        self.AGuardar.config(state = "disabled")
        self.ACancelar.config(state = "disabled")

    def EvZEditar(self):
        """
        Edita una entrada de zoo en la base de datos.

        Parámetros:
            self (objeto): La instancia de la clase.
        
        Retorna:
            Ninguno
        """
        try:
            if self.varZModID.get():
                if self.varZName.get():
                    confirmar = messagebox.askokcancel("Zoos", f"¿Desea Modificar los Datos de: {self.varAModID.get()}?")
                    if confirmar:
                        if self.zoo.editar(self.varZName.get(), "NOMBRE", self.varZModID.get()):
                            self.zooCargar()
                        else:
                            messagebox.showwarning("Error", "No se encontro el Zoologico")

                if self.varUbi.get():
                    confirmar = messagebox.askokcancel("Zoos", f"¿Desea Modificar los Datos de: {self.varAModID.get()}?")
                    if confirmar:
                        if self.zoo.editar(self.varUbi.get(), "UBICACION", self.varZModID.get()):
                            self.zooCargar()
                        else:
                            messagebox.showwarning("Error", "No se encontro el Zoologico")
            else:
                messagebox.showerror("Error", "Falta Informacion.")
        except:
            messagebox.showerror("Error", "No se pudo editar.")
    
    def EvAEditar(self):
        """
        Edita una entrada de Animal en la base de datos.

        Parámetros:
            self (objeto): La instancia de la clase.
        
        Retorna:
            Ninguno
        """
        try:
            if self.varZModID.get():
                if self.varZName.get():
                    confirmar = messagebox.askokcancel("Zoos", f"¿Desea Modificar los Datos de: {self.varAModID.get()}?")
                    if confirmar:
                        if self.zoo.editar(self.varZName.get(), "NOMBRE", self.varZModID.get()):
                            self.zooCargar()
                        else:
                            messagebox.showwarning("Error", "No se encontro el Zoologico")

                if self.varUbi.get():
                    confirmar = messagebox.askokcancel("Zoos", f"¿Desea Modificar los Datos de: {self.varAModID.get()}?")
                    if confirmar:
                        if self.zoo.editar(self.varUbi.get(), "UBICACION", self.varZModID.get()):
                            self.zooCargar()
                        else:
                            messagebox.showwarning("Error", "No se encontro el Zoologico")
            else:
                messagebox.showerror("Error", "Falta Informacion.")
        except:
            messagebox.showerror("Error", "No se pudo editar.")

    def EvZEliminar(self):
        """
        Elimina un registro de zoo de la base de datos si el usuario confirma la eliminación.
        
        Parámetros:
            self (object): La instancia de la clase.
        
        Retorna:
            None
        
        Arroja:
            None
        """
        try:
            if self.varZModID.get():
                confirmar = messagebox.askokcancel("Zoos", f"¿Desea Eliminar el Registro: {self.varZModID.get()}?")
                if confirmar:
                    if self.zoo.eliminar(self.varZModID.get()):
                        self.animal.eliminarTodo(self.varZModID.get())
                        self.zooCargar()
                        self.animalCargar()
                    else:
                        messagebox.showwarning("Error", "No se encontro el Zoologico")
            else:
                messagebox.showerror("Error", "Falta Informacion.")
        except:
            messagebox.showerror("Error", "No se pudo eliminar.")

    def EvAEliminar(self):
        """
        Elimina un registro de Animal de la base de datos si el usuario confirma la eliminación.
        
        Parámetros:
            self (object): La instancia de la clase.
        
        Retorna:
            None
        
        Arroja:
            None
        """
        try:
            if self.varAModID.get():
                confirmar = messagebox.askokcancel("Animals", f"¿Desea Eliminar el Registro: {self.varAModID.get()}?")
                if confirmar:
                    if self.animal.eliminar(self.varAModID.get()):
                        self.animalCargar()
                    else:
                        messagebox.showwarning("Error", "No se encontro el Animal")
            else:
                messagebox.showerror("Error", "Falta Informacion.")
        except:
            messagebox.showerror("Error", "No se pudo eliminar.")