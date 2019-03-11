import pathlib, os, sys, clipboard, psutil, colorama
from termcolor import *
colorama.init()
if os.name == "Posix":
    Posix = True
    import subprocess32 as subprocess
else:
    import subprocess
    Posix = False
path = pathlib.Path.cwd()
path = str(path)
def launchRecordingSoftware():
    if not(path.find("recording") == -1):
        print("FOUND RECORDING")
        launchAHKPath = "..\\..\\src\\launchPulover.ahk"
    else:
        launchAHKPath = "..\\src\\launchPulover.ahk"
    try:
        subprocess.call(['C:\Program Files\AutoHotKey\AutoHotkey.exe',launchAHKPath])
        return True
    except Exception:
        print("Failed to launch recording software, check line 13 and 15 of recordTesting.py, as well as your recoding software in dependecyTesting.py")
        return False
def copyScript(script):
    currentClipboard = clipboard.paste()
    if not(path.find("\\recording\\") == -1):
        getAHKScript = "..\\..\\src\\getAHKScript.ahk"
    else:
        getAHKScript = "..\\src\\getAHKScript.ahk"
        subprocess.call(['C:\Program Files\AutoHotKey\AutoHotkey.exe',getAHKScript])
    if script == "":
        c = "Click"
        contents = clipboard.paste()
        if not(contents.find(c)==-1):
            return True
        else:
            return False
    else:
         scriptToTest = script
         if clipboard.paste() == scriptToTest:
             return True
         else:
             return False
def closeRecordingSoftware():
    if "MacroCreator.exe" in (p.name() for p in psutil.process_iter()):
        print("Closing Recording Software...")
        try:
            os.system("taskkill /im MacroCreator.exe")
            return True
        except Exception:
            print("Couldn't Close Software, check lines in recordTesting.py, as well as your recoding software in dependecyTesting.py")
            return False
    else:
        print("Process not open, passing false positive to end test")
        return True
def main():
    launchRecordingSoftwareV = False
    copyScriptV = False
    if len(sys.argv) == 1:
        if (launchRecordingSoftware()):
            launchRecordingSoftwareV = True
        script = input("Testing Custom Script? (Enter script, or press enter to perform a default test)")
        if(copyScript(script)):
            copyScriptV = True
        if (launchRecordingSoftwareV and copyScriptV):
            print("launchRecordingSoftware: True")
            print("copyScript: True")
            print("-------------")
            print(colored("PASS", 'green'), __file__)
        else:
            print("-------------")
            print(colored("FAIL", 'red'), __file__)
            if not(launchRecordingSoftwareV):
                print("X launchRecordingSoftware")
            if not(copyScriptV):
                print("X copyScript")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-launchRecordingSoftware":
            print("launchRecordingSoftware: ", launchRecordingSoftware())
        elif sys.argv[1] == "-copyScript":
            script = input("Testing Custom Script? (Enter script, or press enter to skip to default)")
            print("copyScript: ", copyScript(script))
        elif sys.argv[1] == "-closeRecordingSoftware":
            print("closeRecordingSoftware: ", closeRecordingSoftware())
        else:
            print("No such dependency test")
if __name__ == "__main__":
    main()
