flagRebirth := false
flagReset := false

funcionRebirth() {
    MouseMove, 1339,412
    Click
    MouseMove, 1049,424
    Click
    MouseMove, 1228,702
    Click
    MouseMove, 1280,489
    Click
    MouseMove, 1282,538
    Click

    
}

funcionResetStats() {
    MouseMove, 465, 800
    Click
    MouseMove, 555, 425
    Click
    MouseMove, 555, 500
    Click
}

^Numpad3::
    if (!flagReset) {
        flagRebirth := !flagRebirth
        if (flagRebirth) {
            funcionRebirth()
            SetTimer, funcionRebirth, 600000
        } else {
            SetTimer, funcionRebirth, Off
            SetTimer, funcionResetStats, Off
        }
    }
return

^Numpad1::
    if (!flagRebirth) {
        flagReset := !flagReset
        if (flagReset) {
            MouseMove, 695, 295
            Click
            MouseMove, 160, 500
            Click
            funcionResetStats()
            SetTimer, funcionResetStats, 15
        } else {
            SetTimer, funcionResetStats, Off
        }
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