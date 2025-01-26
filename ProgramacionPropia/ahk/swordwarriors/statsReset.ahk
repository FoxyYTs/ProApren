flagReset := false

funcionResetStats() {
    MouseMove, 555, 425
    Click
    MouseMove, 555, 500
    Click
    MouseMove, 465, 785
    Click
}

^g::
    flagReset := !flagReset
    if (flagReset) {
        funcionResetStats()
        SetTimer, funcionResetStats, 15
    } else {
        SetTimer, funcionResetStats, Off
    }
return

MouseMove, 160, 500