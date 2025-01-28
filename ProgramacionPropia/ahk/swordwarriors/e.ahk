flagE := false

FuncionE() {
    Send, e
}

^Numpad5::
    flagE := !flagE
    if (flagE) {
        Send, e
        SetTimer, FuncionE, 38500
    } else {
        SetTimer, FuncionE, Off
    }
return