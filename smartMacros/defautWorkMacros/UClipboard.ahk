Menu, clipboard, Add,, MenuHandler
;End clipboard submenu
; Create a submenu in the first menu (a right-arrow indicator). When the user selects it, the second menu is displayed.
Menu, MyMenu, Add, Clipboard, :clipboard
Menu, MyMenu, Add  ; Add a separator line.

MenuHandler:
Sleep, 200
Send, %A_ThisMenuItem%

run2 = True
while run2{
if(getKeyState("CapsLock", "T")){

  if (getKeyState("Control") and getKeyState("c")){
      ;msgbox, "copy"
      sleep, 200
      item = %clipboard%
      Run, python UClipboard.py %item%,, Hide
      }
   }
  else if (not(getKeyState("CapsLock", "T"))){
    continue
   }
  else if(getKeyState("Alt") and getKeyState("q")){
  item = Exception420
  Run, python UClipboard.py %item%,, Hide
  run2 = 0
  break
   }
   }
^v::Menu, MyMenu, Show  ; i.e. press the Win-Z hotkey to show the menu.
return
!q:: Run, python UClipboard.py Exception420,, Hide
ExitApp
