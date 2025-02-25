Ejecutar() {
    ; Definir el comando SSH con ssh (OpenSSH)
    comando := "ssh foxyyts@192.168.1.143 cat /home/foxyyts/ahk/text.txt > D:\ahk\cmd_output.txt 2>&1"
    
    ; Mostrar el comando en un MsgBox (opcional, para depuración)
    MsgBox, %comando%

    ; Ejecutar el comando usando cmd.exe
    RunWait, %ComSpec% /c %comando%,, Hide
}

; Llamar a la función
Ejecutar()