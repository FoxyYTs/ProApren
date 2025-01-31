flagHabilidad := false

funcionQ() {
    Send, q
}

funcionE() {
    Send, e
}

^Numpad2::
    flagHabilidad := !flagHabilidad
    if (flagHabilidad) {
        funcionE()
        SetTimer, funcionE, 38500
        SetTimer, funcionQ, 53500
    } else {
        SetTimer, funcionQ, Off
        SetTimer, funcionE, Off
    }
return

; CDQ = 60 segs
; ACTQ = 3 segs


; CDE = 38 segs
; ACTE = 3 segs