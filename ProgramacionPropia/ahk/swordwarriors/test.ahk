funcionStart() {
    MouseMove, 960, 65
    Click
    Sleep 50
    MouseMove, 370, 794
    Click
    Sleep 3000
    MouseMove, 965, 120
    Click
    Sleep 50
}

funcionRepost() {
    MouseMove, 1380, 105
    Click
    Sleep 500
    MouseMove, 965, 160
    Click
    Sleep 50
}


^Numpad5::
    if (!flagRepost) {
        flagHero := !flagHero
        if (flagHero) {
            funcionStart()
            SetTimer, funcionStart, 300000
        } else {
            SetTimer, funcionStart, off
        }
    }
return

^Numpad9::
    if (!flagHero) {
        flagRepost := !flagRepost
        if (flagRepost) {
            funcionRepost()
            SetTimer, funcionRepost, 302500
        } else {
            SetTimer, funcionRepost, off
        }
    }
return