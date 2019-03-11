startingClipboard = %clipboard%
stop = 0
clipboard1 =
clipboard2 =
clipboard3 =
clipbaord4 =
empty =
1stClipboard = 0
2ndClipboard = 0
3rdClipboard = 0
4thClipboard = 0
Loop {
sleep, 200
sleep, 200
if(GetKeyState("Alt") and GetKeyState("q")){
 stop = 1
}
else if not(GetKeyState("CapsLock", "T")){
  startingClipboard = %clipboard%
  continue
  }
else if(GetKeyState("CapsLock", "T")){
  4thClipboard = 0
  1stClipboard = 1
  sleep, 200
  ;msgbox, "startingClipboard = " %clipboard%
  clipboard = %clipboard1%
  KeyWait, Alt, D T1
  if !ErrorLevel{
    Sleep, 200
    1stClipboard = 0
    2ndClipboard = 1
    3rdClipboard = 0
    4thClipboard = 0
    clipboard = %clipboard2%
    msgbox, "Set to 2nd "
    KeyWait, Alt, D T0.5
      if !ErrorLevel{
        clipboard = %clipboard3%
        2ndClipboard = 0
        3rdClipboard = 1
        Sleep, 200
        msgbox, "Set to 3rd "
        KeyWait, Alt, D T0.5
        if !ErrorLevel{
          4thClipboard = 1
          3rdClipboard = 0
          clipboard = %clipboard4%
          msgbox, "Set to 4th "
          ;Set clipboard4
        }
      }
    }
  run2 = True
  while run2{
 if (getKeyState("Control") and getKeyState("c")){
      ;msgbox, "copy"
      sleep, 200
      if(4thClipboard){
        clipboard4 = %clipboard4% %clipboard%
      ;  msgbox, "getting 4thClipboard"
      }
      else if(3rdClipboard){
        clipboard3 = %clipboard3% %clipboard%
      ;  msgbox, "getting 3rdClipboard"
      }
      else if(2ndClipboard){
        clipboard2 = %clipboard2% %clipboard%
      ;  msgbox, "getting 2ndClipboard"
      }
      else if(1stClipboard){
          clipboard1 = %clipboard1% %clipboard%
      }
      else{
        clipboard = %clipboard%
      }
     }
    else if (not(getKeyState("CapsLock", "T"))){
      clipboard = %startingClipboard%
      run2 = 0
      break
     }
    else if(GetKeyState("Alt") and GetKeyState("q")){
      clipboard = %startingClipboard%
      stop = 1
      run2 = 0
  }
  }
  }
run1 = 0
} Until stop
msgbox, "Exiting..."
