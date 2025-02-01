flagRebirth := false
flagRebirth2 := false
flagReset := false

funcionRebirth() {
    MouseMove, 695, 295
    Click
    MouseMove, 175, 700
    Click
    Sleep 50
    MouseMove, 1175, 675
    Click
    Sleep 50
    MouseMove, 1295, 145
    Click
    Sleep 50
    MouseMove, 160, 500
    Click
    Sleep 50
}

funcionRebirth2() {
    MouseMove, 175, 700
    Click
    Sleep 50
    MouseMove, 1175, 675
    Click
    Sleep 50
    MouseMove, 1295, 145
    Click
    Sleep 50
}

funcionResetStats() {
    MouseMove, 465, 800
    Click
    MouseMove, 555, 425
    Click
    MouseMove, 555, 500
    Click
}

funcionResetStats2() {
    SetTimer, funcionDelay, Off
    MouseMove, 160, 500
    Click
    Sleep 50
    MouseMove, 465, 800
    Click
    Sleep 50
    MouseMove, 555, 425
    Click
    Sleep 50
    MouseMove, 555, 500
    Click
    Sleep 50
    MouseMove, 695, 295
    Click
    Sleep 50
    SetTimer, funcionDelay, 15
}

funcionDelay() {
    MouseMove, 1295, 145
    Click
}

^Numpad3::
    if (!flagReset && !flagRebirth2) {
        flagRebirth := !flagRebirth
        if (flagRebirth) {
            funcionRebirth()
            funcionResetStats()
            SetTimer, funcionRebirth, 600000
            SetTimer, funcionResetStats, 15
        } else {
            SetTimer, funcionRebirth, Off
            SetTimer, funcionResetStats, Off
        }
    }
return

^Numpad2::
    if (!flagReset && !flagRebirth) {
        flagRebirth2 := !flagRebirth2
        if (flagRebirth2) {
            funcionRebirth2()
            SetTimer, funcionRebirth2, 600000
            SetTimer, funcionResetStats2, 60000
            SetTimer, funcionDelay, 15
        } else {
            SetTimer, funcionRebirth2, Off
            SetTimer, funcionResetStats2, off
            SetTimer, funcionDelay, Off
        }
    }
return

^Numpad1::
    if (!flagRebirth && !flagRebirth2) {
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