flagQ := false

FuncionQ() {
    Send, q
    Sleep 3000
}

FuncionE() {
    Send, e
    Sleep 3000
}

^Numpad4::
    flagQ := !flagQ
    if (flagQ) {
        FuncionQ()
        Sleep 3000
        FuncionE()
        SetTimer, FuncionQ, 60000
        SetTimer, FuncionE, 38000
    } else {
        SetTimer, FuncionQ, Off
        SetTimer, FuncionE, Off
        Msgbox "Macro Habilidades Desactivado"
    }
return