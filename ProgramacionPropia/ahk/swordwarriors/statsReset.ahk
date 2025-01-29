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
        MouseMove, 695, 295
        Click
        MouseMove, 160, 500
        Click
        funcionResetStats()
        SetTimer, funcionResetStats, 15
    } else {
        SetTimer, funcionResetStats, Off
    }
return

MouseMove, 160, 500