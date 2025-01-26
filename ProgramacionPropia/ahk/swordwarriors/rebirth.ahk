flagRebirth := false

funcionRebirth() {
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
}

funciondelay() {
    MouseMove, 1295, 145
    Click
}

^j::
    flagRebirth := !flagRebirth
    if (flagRebirth) {
        funcionRebirth()
        funcionResetStats()
        SetTimer, funcionRebirth, 3600000
        SetTimer, funcionResetStats, 660000
        SetTimer, funciondelay, 15
    } else {
        SetTimer, funcionRebirth, Off
        SetTimer, funcionResetStats, Off
        SetTimer, funciondelay, Off
    }
return