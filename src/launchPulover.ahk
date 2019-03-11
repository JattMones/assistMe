Screenx := A_ScreenWidth
Screeny := A_ScreenHeight
ScreenxPos := Screenx//2
ScreenyPos := Screeny//2
WinActivate,  ahk_class WorkerW
Sleep, 800
Send, {LWin Down}
Sleep, 94
Send, {s}
Sleep, 31
Click, 1423, 0, 0
Sleep, 62
WinActivate, Cortana ahk_class Windows.UI.Core.CoreWindow
Send, {LWin Up}
Sleep, 532
Send, {LShift Down}
Sleep, 203
Send, {p}
Sleep, 31
Send, {LShift Up}
Sleep, 31
Send, {u}
Sleep, 31
Send, {l}
Sleep, 31
Send, {o}
Sleep, 31
Send, {v}
Sleep, 31
Send, {e}
Sleep, 31
Send, {r}
Sleep, 31
Send, {'}
Sleep, 31
Send, {s}
Sleep, 31
Send, {Space}
Sleep, 31
Send, {LShift Down}
Sleep, 31
Send, {m}
Sleep, 31
Send, {LShift Up}
Send, {a}
Sleep, 31
Send, {c}
Sleep, 31
Send, {r}
Sleep, 31
Send, {o}
Sleep, 31
Send, {Space}
Sleep, 125
Send, {LShift Down}
Sleep, 93
Send, {c}
Sleep, 31
Send, {LShift Up}
Send, {r}
Sleep, 31
Send, {e}
Sleep, 31
Send, {a}
Sleep, 31
Send, {t}
Sleep, 31
Send, {o}
Sleep, 31
Send, {r}
Sleep, 31
Send, {Enter}
Sleep, 5000
WinActivate,  ahk_class WorkerW
Click, %ScreenxPos%, %ScreenyPos% Left, Down
Sleep, 78
Click, %ScreenxPos%, %ScreenyPos% Left, Up
