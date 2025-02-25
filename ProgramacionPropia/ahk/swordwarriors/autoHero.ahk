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

; Funcion para ejecutar comandos SSH
ejecutarSSH(comando) {
    ; Ejecutar comando SSH usando OpenSSH
    comandoSSH := "ssh foxyyts@192.168.1.143 " comando
    MsgBox, Ejecutando comando SSH: %comandoSSH%
    RunWait, %ComSpec% /c %comandoSSH%,, Hide
    If (ErrorLevel != 0) {
        MsgBox, Error al ejecutar comando SSH: %comandoSSH%
        ExitApp
    }
}

; Funcion para crear un archivo en el servidor SSH
crearArchivoSSH(archivoRemoto, contenido) {
    ; Crear archivo en el servidor SSH
    comandoSSH := "ssh foxyyts@192.168.1.143 'echo " contenido " > /home/foxyyts/ahk/" archivoRemoto "'"
    MsgBox, Creando archivo: %sshPath%%archivoRemoto%
    MsgBox, %comandoSSH%
    RunWait, %ComSpec% /c %comandoSSH%,, Hide
    If (ErrorLevel != 0) {
        MsgBox, Error al crear archivo: %archivoRemoto%
        ExitApp
    }
}

; Funcion para leer un archivo en el servidor SSH
leerArchivoSSH(archivoRemoto) {
    ; Construir el comando SSH
    comandoSSH := "ssh foxyyts@192.168.1.143 cat /home/foxyyts/ahk/" archivoRemoto " 2>&1 > D:\cmd_output.txt"
    MsgBox, Leyendo archivo: %sshPath%%archivoRemoto%

    ; Ejecutar el comando SSH y redirigir la salida a un archivo temporal
    RunWait, % comandoSSH, , Hide

    MsgBox, test
    ; Leer la salida del archivo temporal
    FileRead, contenido, "D:\cmd_output.txt"
    MsgBox, test2
    if (ErrorLevel) {
        MsgBox, Error al leer el archivo de salida.
        return
    }

    MsgBox, test3

    ; Mostrar el contenido leído
    MsgBox, Contenido del archivo remoto:`n%contenido%

    ; Eliminar el archivo temporal (opcional)
    FileDelete, D:\cmd_output.txt
    Return contenido
}

; Funcion principal
funcionStart() {
    MsgBox, Iniciando Funcion Start en %A_ComputerName%.
    Sleep, 2000  ; Simula algún procesamiento

    ; Crear archivo de inicio en el servidor SSH
    crearArchivoSSH(startFile, "Iniciado")

    ; Esperar a que FuncionRepost termine (verificar archivo en el servidor SSH)
    Loop {
        ; Leer el archivo temporal en el servidor
        contenido := leerArchivoSSH(repostFile)
        
        ; Verificar si el archivo contiene "Terminado"
        If (contenido = "Terminado") {
            ejecutarSSH("rm /home/foxyyts/ahk/" repostFile)  ; Eliminar archivo de confirmación
            Break
        }
        Sleep, 1000  ; Esperar 1 segundo antes de verificar nuevamente
    }

    MsgBox, Continuando Funcion Start en %A_ComputerName%.
    Sleep, 2000  ; Simula más procesamiento

    MsgBox, Funcion Start completada en %A_ComputerName%.
}

funcionRepost() {
    MsgBox, Iniciando Funcion Repost en %A_ComputerName%.
    Sleep, 2000  ; Simula algún procesamiento

    ; Crear archivo de confirmación en el servidor SSH
    crearArchivoSSH(repostFile, "Terminado")

    MsgBox, Funcion Repost completada en %A_ComputerName%.
}

; Verificar si este computador debe ejecutar FuncionRepost
contenido := leerArchivoSSH(startFile)
If (contenido = "Iniciado") {
    ejecutarSSH("rm /home/foxyyts/ahk/" startFile)  ; Eliminar archivo de inicio
    funcionRepost()
} Else {
    ; Si no hay archivo, ejecutar FuncionStart
    funcionStart()
}