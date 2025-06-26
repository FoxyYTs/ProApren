flagRebirth := false
flagRebirth2 := false
flagReset := false

funcionClaim() {
    MouseMove, 1882, 104
    Click
    Sleep 500
    MouseMove, 1653, 972
    Click
    Sleep 500
    MouseMove, 1892, 51
    Click
    Sleep 500
    MouseMove, 1404, 229
    Click
    Sleep 500
}

funcionDelay() {
    MouseMove, 1050, 50
    Click
}

^Numpad2::
    flagRebirth2 := !flagRebirth2
    if (flagRebirth2) {
        funcionClaim()
        SetTimer, funcionDelay, 14000
        SetTimer, funcionClaim, 1800000
    } else {
        SetTimer, funcionClaim, Off
        SetTimer, funcionDelay, Off
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