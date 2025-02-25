sudo /opt/lampp/lampp stop

sshUser := "foxyyts"  ; Usuario SSH
sshPass := "1987"  ; Contraseña SSH
sshHost := "192.168.1.143"  ; Dirección IP o nombre del servidor SSH
sshPath := "/home/foxyyts/ahk"  ; Ruta en el servidor SSH para los archivos de confirmación

EjecutarSSH(comando) {
    ; Ejecutar comando SSH usando OpenSSH
    comandoSSH := "ssh " sshUser "@" sshHost " " comando
    MsgBox, Ejecutando comando SSH: %comandoSSH%
    RunWait, % comandoSSH,, Hide
    If (ErrorLevel != 0) {
        MsgBox, Error al ejecutar comando SSH: %comandoSSH%
        ExitApp
    }
}