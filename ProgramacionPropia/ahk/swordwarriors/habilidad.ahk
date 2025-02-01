flagHabilidad := false

funcionQ() {
    Send, q
}

funcionE() {
    Send, e
}

^Numpad4::
    flagHabilidad := !flagHabilidad
    if (flagHabilidad) {
        funcionE()
        SetTimer, funcionE, 4000
        SetTimer, funcionQ, 6000
    } else {
        SetTimer, funcionQ, Off
        SetTimer, funcionE, Off
    }
return

; CDQ = 60 segs
; ACTQ = 3 segs


; CDE = 38 segs
; ACTE = 3 segs