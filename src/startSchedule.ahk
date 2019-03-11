Screenx := A_ScreenWidth
Screeny := A_ScreenHeight
ScreenxPos := Screenx//2 + Screenx//4 
ScreenyPos := Screeny//2
Msgbox, %ScreenxPos% %ScreenyPos%
coordMode, Mouse, Screen
Send, {LWin Down}
Sleep, 157
Click, 1218, 713, 0
Send, r
Sleep, 343
Send, {LWin Up}
Send, taskschd.msc
Send, {Enter}
Sleep, 5000
Click, %ScreenxPos%, %ScreenyPos% Left, Down
Sleep, 78
Click, %ScreenxPos%, %ScreenyPos% Left, Up
;WinGetPos, X, Y, , , A  ; "A" to get the active window's pos.
;MouseGetPos, xpos, ypos
;xClick := %xpos%-%X%
;yClick := %ypos%-%Y%
;MsgBox, The active window is at %xClick%`,%yClick%
