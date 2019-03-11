count = 0
; Create another menu destined to become a submenu of the above menu.
Menu, work, Add  ; Add a separator line.
;End work submenu

Menu, misc, Add  ; Add a separator line.
;End misc submenu

Menu, tmp, Add  ; Add a separator line.
;End tmp submenu

; Create a submenu in the first menu (a right-arrow indicator). When the user selects it, the second menu is displayed.
Menu, MyMenu, Add, Work, :work
Menu, MyMenu, Add  ; Add a separator line.
Menu, MyMenu, Add, Misc., :misc
Menu, MyMenu, Add  ; Add a separator line.
Menu, MyMenu, Add, Temp., :tmp

MenuHandler:
;run, cmd.exe
;Sleep, 500
;Send, cd %userprofile%\myMacros\%A_ThisMenu%
;Send, {Enter}
;Sleep, 500
;Send, start %A_ThisMenuItem%
;Send, {Backspace}
;Send, .ahk
;Send, {Enter}
if (count != 0){
  path = %Temp%\\myMacros\\%A_ThisMenu%\\%A_ThisMenuItem%
  Run, python runMacro.py %path%,, Hide
}
else {
  count = 1
}
return

^q::Menu, MyMenu, Show  ; i.e. press the Win-Z hotkey to show the menu.
