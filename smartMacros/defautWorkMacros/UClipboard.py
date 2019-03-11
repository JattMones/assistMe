import sys, pathlib, psutil, subprocess
def main(item):
    if "AutoHotkey.exe" in (p.name() for p in psutil.process_iter()):
        try:
            os.system("taskkill /im AutoHotKey.exe")
        except Exception:
            print("Couldn't Close Software")
    print(type(item))
    print(item)
    path = pathlib.Path.cwd()
    rightClickPath= pathlib.PurePath(path,"UClipboard.ahk")
    f = open(rightClickPath, "r")
    rightClickContents = f.readlines()
    f.close()
    if (item.find("Exception420") == -1):
        print("Trying to add")
        for i in range(len(rightClickContents)):
          if rightClickContents[i] == "Menu, clipboard, Add,, MenuHandler\n":
              rightClickContents.insert(i, ("Menu, clipboard, Add, "+item+", MenuHandler\n"))
              rightClickContents.insert(i, "Menu, clipboard, Add  ; Add a separator line.\n")
              i = len(rightClickContents)-1
              print(rightClickContents)
              break
        f = open(rightClickPath, "w+")
        rightClickContents = "".join(rightClickContents)
        f.write(rightClickContents)
        f.close()
        subprocess.Popen(['C:\Program Files\AutoHotKey\AutoHotkey.exe','UClipboard.ahk'])
    elif item == "Exception420":
        print("EXCEPTION CAUGHT")
        for i in range(len(rightClickContents)):
            if rightClickContents[i] == "Menu, clipboard, Add,, MenuHandler\n":
                rightClickContents = rightClickContents[i:]
                i = len(rightClickContents)-1
                break
        f = open(rightClickPath, "w+")
        rightClickContents = "".join(rightClickContents)
        f.write(rightClickContents)
        f.close()
        if "AutoHotkey.exe" in (p.name() for p in psutil.process_iter()):
            try:
                os.system("taskkill /im AutoHotKey.exe")
            except Exception:
                print("Couldn't Close Software")
if __name__ == "__main__":
    main(sys.argv[1])
