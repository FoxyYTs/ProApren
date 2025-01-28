flagF := false

FuncionF() {
    Send, f
}

^Numpad6::
    flagF := !flagF
    if (flagF) {
        Send, f
        SetTimer, FuncionF, 27500
        
    } else {
        SetTimer, FuncionF, Off
    }
return