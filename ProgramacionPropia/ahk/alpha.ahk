flagAlpha := false
flagClick := false
Delay := 100

funcionMejora(){
    MouseMove, 1261, 795
    Click
    Sleep, 100
    Click
    Sleep, 100
    Click
    Sleep, 100
    Click
    Sleep, 100
    Click
}

funcionArbol(){
    MouseMove, 567, 359
    Click
    Sleep, 100
    MouseMove, 785, 185
    Click
}

funcionAlpha() {
    funcionMejora()
    Sleep, 100
    funcionArbol()
    Sleep, 100
    funcionArbol()
    Sleep, 100
    funcionArbol()
    Sleep, 100
    funcionArbol()
    Sleep, 100
}

funcionClick(){
    Click
    Sleep, 100
}

^Numpad2::
        if(!flagClick){
            flagAlpha := !flagAlpha
            if (flagAlpha) {
                SetTimer, funcionAlpha, 15
            } else {
                SetTimer, funcionAlpha, Off
            }
        }
        
Return

^Numpad1::
        if(!flagAlpha){
            flagClick := !flagClick
            if (flagClick) {
                SetTimer, funcionClick, 15
            } else {
                SetTimer, funcionClick, Off
            }
        }
Return

; Screen:	567, 359
; Window:	-1345, 367

; Screen:	785, 185
; Window:	-1127, 193

; Screen:	1261, 795
; Window:	-651, 803