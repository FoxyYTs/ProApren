flagRebirth := false

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

funcionResetStats() {
    MouseMove, 465, 800
    Click
    MouseMove, 555, 425
    Click
    MouseMove, 555, 500
    Click
}

funciondelay() {
    MouseMove, 1295, 145
    Click
}

^Numpad3::
    flagRebirth := !flagRebirth
    if (flagRebirth) {
        Process, Close, statsReset.exe
        funcionRebirth()
        funcionResetStats()
        SetTimer, funcionRebirth, 600000
        SetTimer, funcionResetStats, 15
    } else {
        SetTimer, funcionRebirth, Off
        SetTimer, funcionResetStats, Off
        run "B:\programacion\ProApren\ProgramacionPropia\ahk\swordwarriors\statsReset.exe"
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