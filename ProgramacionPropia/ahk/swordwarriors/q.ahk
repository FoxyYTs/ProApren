flagQ := false

FuncionQ() {
    Send, q
}

^q::
    flagQ := !flagQ
    if (flagQ) {
        SetTimer, FuncionQ, 70000
    } else {
        SetTimer, FuncionQ, Off
    }
return
