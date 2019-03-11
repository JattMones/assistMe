Screenx := A_ScreenWidth
Screeny := A_ScreenHeight
ScreenxPos := Screenx//2 + Screenx//4
ScreenyPos := Screeny//2
Sleep, 1000
Send, {LWin Down}
Sleep, 157
Click, 1218, 713, 0
Send, {Up}
Sleep, 343
Send, {LWin Up}
Sleep, 1938
Click, 1218, 711, 0
Sleep, 16
Click, 1218, 713, 0
Click, %ScreenxPos%, %ScreenyPos% Left, Down
Sleep, 78
Click, %ScreenxPos%, %ScreenyPos% Left, Up
Sleep, 1703
Send, {LControl Down}
Sleep, 156
Send, {a}
Sleep, 313
Send, {LControl Up}
Sleep, 515
Send, {LControl Down}
Sleep, 531
Send, {c}
Sleep, 188
Send, {LControl Up}
Sleep, 219
