start = 0
stop = 0
clipboard2 = ""
empty =
Loop {
sleep, 200
sleep, 200
if(GetKeyState("Alt") and GetKeyState("q")){
 stop = 1
}
else if not(GetKeyState("CapsLock", "T")){
  continue
}
else if(GetKeyState("CapsLock", "T")){
  start += 1
  if(start == 1){
    currentClipboard = 
  }
  else{
  currentClipboard = %clipboard%
  }
  run1 = 1
  while run1{
    if (getKeyState("Control") and getKeyState("c")){
        sleep, 200
        clipboard = %currentClipboard%  %clipboard%
        currentClipboard = %clipboard%
      }
    else if not(getKeyState("CapsLock", "T")){
          run1 = False
          break
         }
    else if(GetKeyState("Alt") and GetKeyState("q")){
      stop = 1
      run1 = 0
  }
}
}
run1 = 0
} Until stop
msgbox, "Exiting..."
