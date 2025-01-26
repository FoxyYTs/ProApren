flagQ := false

FuncionQ() {
    Send, q
}

^q::
    flagQ := !flagQ
    if (flagQ) {
        Send, q
        SetTimer, FuncionQ, 61000
    } else {
        SetTimer, FuncionQ, Off
    }
return
