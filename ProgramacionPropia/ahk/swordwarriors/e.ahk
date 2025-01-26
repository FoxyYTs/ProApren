flagE := false

FuncionE() {
    Send, e
}

^e::
    flagE := !flagE
    if (flagE) {
        Send, e
        SetTimer, FuncionE, 5500
    } else {
        SetTimer, FuncionE, Off
    }
return