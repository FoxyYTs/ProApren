flagReset := false

funcionResetStats() {
    MouseMove, 465, 800
    Click
    MouseMove, 555, 425
    Click
    MouseMove, 555, 500
    Click
}

^Numpad1::
    flagReset := !flagReset
    if (flagReset) {
        Process, Close, rebirth.exe
        MouseMove, 695, 295
        Click
        MouseMove, 160, 500
        Click
        funcionResetStats()
        SetTimer, funcionResetStats, 15
    } else {
        SetTimer, funcionResetStats, Off
        run "B:\programacion\ProApren\ProgramacionPropia\ahk\swordwarriors\exe\rebirth.exe"
    }
return