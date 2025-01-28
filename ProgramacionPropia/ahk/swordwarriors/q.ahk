flagQ := false

FuncionQ() {
    Send, q
}

^Numpad4::
    flagQ := !flagQ
    if (flagQ) {
        Send, q
        SetTimer, FuncionQ, 60500
    } else {
        SetTimer, FuncionQ, Off
    }
return
