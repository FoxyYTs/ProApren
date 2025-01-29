flagQ := false

FuncionQ() {
    Send, q
    Sleep 5000
}

FuncionE() {
    Send, e
    Sleep 5000
}

^Numpad4::
    flagQ := !flagQ
    if (flagQ) {
        FuncionQ()
        Sleep 5000
        FuncionE()
        SetTimer, FuncionQ, 60000
        SetTimer, FuncionE, 38000
    } else {
        SetTimer, FuncionQ, Off
        SetTimer, FuncionE, Off
    }
returnf