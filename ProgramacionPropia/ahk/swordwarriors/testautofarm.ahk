#NoEnv
#Warn
SendMode Input
SetWorkingDir %A_ScriptDir%

; --- HOTKEY ---
^Numpad1::
; Cuando se presiona Ctrl + Numpad1, se ejecuta el código debajo de esta línea hasta el "Return".

; 1. Abrir el Bloc de Notas si no está abierto.
IfWinNotExist, ahk_class Notepad
{
    Run Notepad
    WinWait ahk_class Notepad, , 5
    IfWinNotExist, ahk_class Notepad
    {
        MsgBox, 16, Error, No se pudo abrir el Bloc de Notas. Asegúrate de que está instalado y accesible.
        Return
    }
}

; 2. Esperar un momento para que el Bloc de Notas cargue completamente.
Sleep 500

; 3. Escribir "Hola Mundo" en el área de texto del Bloc de Notas.
ControlSend, Edit1, Hola Mundo, ahk_class Notepad

; 4. Esperar un momento antes de enviar el comando del menú.
Sleep 200

; 5. Abrir el menú "Archivo" del Bloc de Notas usando PostMessage.
; WM_COMMAND = 0x111
; ID del menú Archivo en Notepad (generalmente es 0xEF00 o 61184 en decimal para "Archivo")
; Nota: Algunos recursos mencionan 0xF000 para "Archivo", pero 0xEF00 es más común para el primer menú.
; Si 0xEF00 no funciona, prueba 0xF000 o 61440.
; Para el Bloc de notas, el mensaje WM_COMMAND para Archivo (File) es 0xF100 (61696) o a veces 0xEF00 (61184).
; Vamos a usar 0xF100 que es más estándar para "File" en algunos contextos.

; Primero, obtener el ID de la ventana del Bloc de Notas
WinGet, NotepadID, ID, ahk_class Notepad

; Enviar el mensaje WM_COMMAND al Bloc de Notas para abrir el menú "Archivo"
; PostMessage, Msg, wParam, lParam, Control, WinTitle, WinText
; Msg (0x111 = WM_COMMAND)
; wParam (ID del comando del menú - 0xF100 para Archivo)
; lParam (0) - No se necesita para este caso
PostMessage, 0x111, 0xF100, 0, , ahk_id %NotepadID%


; 6. Mensaje de confirmación.
MsgBox, 64, Completado, "Hola Mundo" ha sido escrito y se ha intentado abrir el menú Archivo.

Return