flagF := false

FuncionF() {
    Send, f
}

^f::
    flagF := !flagF
    if (flagF) {
        Send, f
        SetTimer, FuncionF, 28000
        
    } else {
        SetTimer, FuncionF, Off
    }
return