flagF := false

FuncionF() {
    Send, f
}

^f::
    flagF := !flagF
    if (flagF) {
        SetTimer, FuncionF, 27000
    } else {
        SetTimer, FuncionF, Off
    }
return