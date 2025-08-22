flagCursed := True

funcionCursed() {
    MouseMove, 1112, 57
    Click
    Sleep 50
    MouseMove, 585, 787
    Click
    Sleep 50
    MouseMove, 1098, 84
    Click
    Sleep 50
}
;#Menu
;Window:	1120, 88
;Client:	1112, 57 (default)

;#Invitacion
;Window:	593, 818
;Client:	585, 787 (default)

;#Listo
;Window:	1106, 115
;Client:	1098, 84 (default)

^Numpad7::
    flagCursed := !flagCursed
    if (flagCursed) {
        funcionCursed()
        SetTimer, funcionCursed, 60000
    } else {
        SetTimer, funcionCursed, Off
    }
    
return

; 3horas = 10800000
; 2horas = 7200000
; 1hora = 3600000
; 45mins = 2700000
; 30mins = 1800000
; 15mins = 900000
; 10mins = 600000
; 5mins = 300000
; 1mins = 60000