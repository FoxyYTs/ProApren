flagClick := false

funcionDelay() {
    MouseMove, 1295, 145
    Click
}

^Numpad5::
        flagClick := !flagClick
        if (flagClick) {
            SetTimer, funcionDelay, 15
        } else {
            SetTimer, funcionDelay, Off
        }
return