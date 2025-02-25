flagHero := false
flagRepost := false

; Configuración SSH
sshUser := "foxyyts"  ; Usuario SSH
sshPass := "1987"  ; Contraseña SSH
sshHost := "192.168.1.143"  ; Dirección IP o nombre del servidor SSH
sshPath := "/home/foxyyts/ahk/"  ; Ruta en el servidor SSH para los archivos de confirmación

; Archivos de confirmación
startFile := "start.txt"  ; Archivo para indicar el inicio de FuncionStart
repostFile := "repost.txt"  ; Archivo para indicar el inicio y fin de FuncionRepost

; Función para ejecutar comandos SSH
ejecutarSSH(comando) {
    ; Ejecutar comando SSH usando OpenSSH
    comandoSSH := "ssh " sshUser "@" sshHost " " comando
    MsgBox, Ejecutando comando SSH: %comandoSSH%
    RunWait, % comandoSSH,, Hide
    If (ErrorLevel != 0) {
        MsgBox, Error al ejecutar comando SSH: %comandoSSH%
        ExitApp
    }
}

; Función para crear un archivo en el servidor SSH
crearArchivoSSH(archivoRemoto, contenido) {
    ; Crear archivo en el servidor SSH
    comandoSSH := "ssh " sshUser "@" sshHost " 'echo " contenido " > " sshPath archivoRemoto "'"
    MsgBox, Creando archivo: %sshPath%%archivoRemoto%
    RunWait, % comandoSSH,, Hide
    If (ErrorLevel != 0) {
        MsgBox, Error al crear archivo: %archivoRemoto%
        ExitApp
    }
}

; Función para leer un archivo en el servidor SSH
leerArchivoSSH(archivoRemoto) {
    ; Construir el comando SSH
    comandoSSH := "ssh " sshUser "@" sshHost " cat " sshPath archivoRemoto " 2>&1 > D:\cmd_output.txt"
    MsgBox, Leyendo archivo: %sshPath%%archivoRemoto%

    ; Ejecutar el comando SSH y redirigir la salida a un archivo temporal
    RunWait, % comandoSSH, , Hide

    ; Leer la salida del archivo temporal
    FileRead, contenido, D:\cmd_output.txt
    if (ErrorLevel) {
        MsgBox, Error al leer el archivo de salida.
        return
    }

    ; Mostrar el contenido leído
    MsgBox, Contenido del archivo remoto:`n%contenido%

    ; Eliminar el archivo temporal (opcional)
    FileDelete, D:\cmd_output.txt
    Return contenido
}

; Función principal
funcionStart() {
    MsgBox, Iniciando Función Start en %A_ComputerName%.
    Sleep, 2000  ; Simula algún procesamiento

    ; Crear archivo de inicio en el servidor SSH
    crearArchivoSSH(startFile, "Iniciado")

    ; Esperar a que FuncionRepost termine (verificar archivo en el servidor SSH)
    Loop {
        ; Leer el archivo temporal en el servidor
        contenido := leerArchivoSSH(repostFile)
        
        ; Verificar si el archivo contiene "Terminado"
        If (contenido = "Terminado") {
            ejecutarSSH("rm " sshPath repostFile)  ; Eliminar archivo de confirmación
            Break
        }
        Sleep, 1000  ; Esperar 1 segundo antes de verificar nuevamente
    }

    MsgBox, Continuando Función Start en %A_ComputerName%.
    Sleep, 2000  ; Simula más procesamiento

    MsgBox, Función Start completada en %A_ComputerName%.
}

funcionRepost() {
    MsgBox, Iniciando Función Repost en %A_ComputerName%.
    Sleep, 2000  ; Simula algún procesamiento

    ; Crear archivo de confirmación en el servidor SSH
    crearArchivoSSH(repostFile, "Terminado")

    MsgBox, Función Repost completada en %A_ComputerName%.
}

; Verificar si este computador debe ejecutar FuncionRepost
contenido := leerArchivoSSH(startFile)
If (contenido = "Iniciado") {
    ejecutarSSH("rm " sshPath startFile)  ; Eliminar archivo de inicio
    funcionRepost()
} Else {
    ; Si no hay archivo, ejecutar FuncionStart
    funcionStart()
}