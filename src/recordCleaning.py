import pathlib, sys, os, subprocess, clipboard, psutil
import ctypes
from ctypes.wintypes import HWND, LPWSTR, UINT
from distutils.dir_util import copy_tree
#Setting up MessageBoxW keyvalues, (ctype message box system).
_user32 = ctypes.WinDLL('user32', use_last_error=True)

_MessageBoxW = _user32.MessageBoxW
_MessageBoxW.restype = UINT  # default return type is c_int, this is not required
_MessageBoxW.argtypes = (HWND, LPWSTR, LPWSTR, UINT)

MB_OK = 0
MB_OKCANCEL = 1
MB_YESNOCANCEL = 3
MB_YESNO = 4

IDOK = 1
IDCANCEL = 2
IDABORT = 3
IDYES = 6
IDNO = 7

#MessageBox method
def MessageBoxW(hwnd, text, caption, utype):
    result = _MessageBoxW(hwnd, text, caption, utype)
    if not result:
        raise ctypes.WinError(ctypes.get_last_error())
    return result
def cleanMacro(path, macroPath, macroTitle, tmp, work):
    def removeMouseTracing(path):
        f = open(path, "r")
        contents = f.readlines()
        f.close()
        running = True
        while(running):
            for i in range(len(contents)):
                if contents[i].startswith("Click") and not("Right" in contents[i] or "Left" in contents[i]):
                    del contents[i]
                    break
                elif(len(contents)-1 == i):
                    running = False
                    break
        return contents
    def identifyClicks(contents):
        k = 0
        i = 0
        running2 = True
        indexes = [1]
        while(running2):
            if(i == len(contents)-1):
                i = 0
                return None
            else:
                for i in range(len(contents)):
                    if contents[i].startswith("Click") and ("Up" in contents[i]):
                        if(len(indexes) > 1):
                            print(indexes[-1])
                            if contents[i] == contents[indexes[-1]-1]:
                                print(indexes[-1])
                                del indexes[-1]
                                indexes.append(i+k+1)
                                print("deleted matching")
                                k += 1
                            else:
                                print("not matching")
                                print(contents[i])
                                indexes.append(i+1+k)
                                k += 1
                        else:
                            print("not matching")
                            print(contents[i])
                            indexes.append(i+1+k)
                            k += 1
                    elif("Send, {Enter}" in contents[i]):
                        indexes.append(i+1+k)
                        k+=1
                    elif(i == len(contents)-1):
                        print("End Contents count:", i)
                        running2 = False
                        for j in range(len(indexes)):
                            print(contents[indexes[j]],indexes[j])
                        return (indexes)
    def prepareWindowInfoCollection(contents, macroPath, path, indexes):
        def insertAHKCode(j, contents2, ahkCode):
            run = True
            while run:
                if contents2[j].find("WinActivate") != -1:
                    print("INSERT")
                    j += 1
                    contents2.insert(j, (ahkCode))
                    run = False
                    break
                elif j == (len(contents2)-1):
                    print("ERROR: Reached end of file before insert")
                    run = False
                    break
                else:
                    j += 1
        title = pathlib.PurePath(macroPath,"windowInfo.txt")
        title = str(title)
        ahkCodeRaw = "WinGet, windowID, ID, A\nWinGet, processID, PID, A\nWinGet, processName, ProcessName, A\nWinGetTitle, windowTitle, A\nFileAppend, \n(\n\n%processName%\n%windowTitle%\n), "
        ahkCode = ahkCodeRaw+title+"\n"
        print("CHECK")
        print(contents)
        contents2 = contents[:]
        for i in range(len(indexes)):
            j = indexes[i]
            insertAHKCode(j, contents2, ahkCode )
        f = open("getWindowInfo.ahk", "w+")
        contents2 = "".join(contents2)
        f.write(contents2)
        f.close()
        print("Contents2", contents2)
        print("Contents", contents)
        result2 = ctypes.windll.user32.MessageBoxW(0, "Press OK to test your Macro","", MB_OKCANCEL)
        try:
            if result2 == IDOK:
                subprocess.call(['C:\Program Files\AutoHotKey\AutoHotkey.exe','getWindowInfo.ahk'])
                f = open(title, 'r')
                contents2 = f.readlines()
                f.close()
                return contents2
            elif result2 == IDCANCEL:
                removeWorkingPath(pathlib.Path(path))
                return None
            else:
                print("Unknown MessageBox return code")
                return None
        except WindowsError as win_err:
            print("An error occurred:\n{}".format(win_err))
            return None
    def checkAndRemoveFileTraversal(contents2, contents, indexes):
        count = 0
        i = 3
        remove = []
        chainStart = False
        while i in range(len(contents2)-1):
            print(i)
            print(contents2[i])
            if (contents2[i].startswith("Explorer.EXE\n") and contents2[i-2].startswith("Explorer.EXE\n") and ((contents2[i+1] != ("\n")) and (contents2[i+1] != ("Program Manager\n")))):
                print("append remove list")
                print(count, indexes[count])
                remove.append(count)
                chainStart = True
            elif(chainStart):
                print("Chain ended")
                del remove[-1]
                chainStart = False
            else:
                print("pass")
                pass
            i += 2
            count += 1
        if(chainStart):
            print("Chain ended")
            del remove[-1]
            chainStart = False
        print(remove)
        for j in sorted(range(len(remove)), reverse = True):
            print("Here")
            print(remove[j])
            start2 = indexes[remove[j]]
            while start2 != 0:
                if contents[start2].find("Click") != -1:
                    del contents[start2]
                    start = start2-1
                    while start != 0:
                        if contents[start].find("Click") != -1:
                            del contents[start]
                            start = 0
                            break
                        else:
                            start -= 1
                    start2 = 0
                    break
                else:
                    start2 -= 1
            #else:
            #    print("Click to remove not found")
            #    print(indexes[remove[j]])
            #    print(contents[indexes[remove[j]]-1])
        return contents
    contents = removeMouseTracing(path)
    indexes = (identifyClicks(contents))
    contents2 = prepareWindowInfoCollection(contents, macroPath, path, indexes)
    if contents2 != None:
        contents3 = checkAndRemoveFileTraversal(contents2, contents, indexes)
        path = (str(path))
        print(path)
        print(macroTitle, macroPath, tmp)
        saveAutomation(contents3, path, macroTitle, macroPath, tmp, work)
    else:
         removeWorkingPath(macroPath)
    return True
def recordRaw():
    result2 = ctypes.windll.user32.MessageBoxW(0, "Would you like to clean your recording?","", MB_YESNO)
    try:
        if result2 == IDYES:
            #Launch save macro callback <-- Unneeded?
            return True
        else:
            #Delete macro file path <-- Unneeded?
            return False
    except WindowsError as win_err:
        print("An error occurred:\n{}".format(win_err))
def pathExists(path):
    if path.is_dir():
        return True
    else:
        return False
def copyScript(path, macroPath, macroTitle, tmp, work):
    global currentClipboard
    currentClipboard = clipboard.paste()
    result2 = ctypes.windll.user32.MessageBoxW(0, "Once macro is recorded and Pulovers main window is open, press ok to continue...","", MB_OKCANCEL)
    try:
        if result2 == IDOK:
            subprocess.call(['C:\Program Files\AutoHotKey\AutoHotkey.exe','getAhkScript.ahk'])
            title = macroTitle + ".ahk"
            path = pathlib.PurePath(path, title)
            path = pathlib.Path(path)
            open(path,"x")
            with open(path, "a") as rawRecording:
                rawRecording.write("\n"+clipboard.paste())
            clipboard.copy(currentClipboard)
        elif result2 == IDCANCEL:
            #Delete Macro Folder Method <-- Unneeded?
            return False
        else:
            print("unknown MessageBox return code")
            print(result)
            return False
    except WindowsError as win_err:
        print("An error occurred:\n{}".format(win_err))
        return False
    if recordRaw():
        print(cleanMacro(path, macroPath, macroTitle, tmp, work))
        return True
    else:
        f = open(path, "r")
        contents = f.readlines()
        f.close()
        saveAutomation(contents, path, macroTitle, macroPath, tmp, work)
        return True
def launchRecordingSoftware(path, macroTitle):
    path.mkdir(parents = False, exist_ok = False)
    macroPath = path
    result = ctypes.windll.user32.MessageBoxW(0, "Starting Record and Clean for " + str(macroTitle) +"...", "", MB_OKCANCEL)
    try:
        if result == IDOK:
            subprocess.call(['C:\Program Files\AutoHotKey\AutoHotkey.exe','launchPulover.ahk'])
            return True
        elif result == IDCANCEL:
            return False
        else:
            print("unknown MessageBox return code")
            print(result)
            return False
    except WindowsError as win_err:
        print("An error occurred:\n{}".format(win_err))
        return False
def closeRecordingSoftware():
    if "MacroCreator.exe" in (p.name() for p in psutil.process_iter()):
        try:
            os.system("taskkill /im MacroCreator.exe")
            return True
        except Exception:
            print("Couldn't Close Software")
            return False
    else:
        return True

def removeWorkingPath(path):
        dir = pathlib.Path(path)
        for item in path.iterdir():
            if item.is_dir():
                removeWorkingPath(item)
            else:
                item.unlink()
        path.rmdir()
def saveAutomation(contents3, path, macroTitle, macroPath, tmp, work):
    result2 = ctypes.windll.user32.MessageBoxW(0, "Would you like to save your automation","", MB_YESNO)
    path = str(path)
    try:
        if result2 == IDYES:
            f = open((path), "w+")
            contents3 = "".join(contents3)
            f.write(contents3)
            f.close()
            path = pathlib.Path.cwd()
            rightClickPath= pathlib.PurePath(path,"rightClickLauncher.ahk")
            f = open(rightClickPath, "r")
            rightClickContents = f.readlines()
            f.close()
            if work:
                for i in range(len(rightClickContents)):
                    if rightClickContents[i] == ";End work submenu\n":
                        rightClickContents.insert(i, ("Menu, work, Add, "+macroTitle+", MenuHandler\n"))
                        rightClickContents.insert(i, "Menu, work, Add  ; Add a separator line.\n")
                        i = len(rightClickContents)-1
                        print(rightClickContents)
                        break
            elif tmp:
                for i in range(len(rightClickContents)):
                    if rightClickContents[i] == ";End tmp submenu\n":
                        rightClickContents.insert(i, ("Menu, tmp, Add, "+macroTitle+", MenuHandler\n"))
                        rightClickContents.insert(i, "Menu, tmp, Add  ; Add a separator line.\n")
                        i = len(rightClickContents)-1
                        print(rightClickContents)
                        break
            else:
                for i in range(len(rightClickContents)):
                    if rightClickContents[i] == ";End misc submenu\n":
                        rightClickContents.insert(i, ("Menu, misc, Add, "+macroTitle+", MenuHandler\n"))
                        rightClickContents.insert(i, "Menu, misc, Add  ; Add a separator line.\n")
                        i = len(rightClickContents)-1
                        print(rightClickContents)
                        break
            f = open(rightClickPath, "w+")
            rightClickContents = "".join(rightClickContents)
            f.write(rightClickContents)
            f.close()
            path = str(path)
            path = path[:-4]
            path = pathlib.PurePath(path, "myMacros")
            fromDirectory = path
            path2 = os.environ['Temp']
            path2 = pathlib.PurePath(path2, "myMacros")
            path2 = pathlib.Path(path2)
            if pathExists(path2):
                removeWorkingPath(path2)
            path2.mkdir()
            path2 = str(path2)
            toDirectory = path2
            copy_tree(fromDirectory, toDirectory)
            print(os.environ['Temp'])
        elif result2 == IDNO:
            removeWorkingPath(macroPath)
        else:
            print("Unknown MessageBox return code")
    except WindowsError as win_err:
        print("An error occurred:\n{}".format(win_err))
def main(tmp, title):
    if (tmp == "Work"):
        tmp = False
        work = True
        macroTitle = str(title)
        path = pathlib.Path.cwd()
        path = str(path)
        path = path[:-4]
        path = pathlib.PurePath(path, "myMacros", "work", macroTitle)
        path = pathlib.Path(path)
        macroPath = path
        if pathExists(path):
            result2 = ctypes.windll.user32.MessageBoxW(0, "Macro already exists with this title, please choose a new title.","", MB_OK)
        else:
            if launchRecordingSoftware(path, macroTitle):
                if copyScript(path, macroPath, macroTitle, tmp, work):
                    pass
                else:
                    if pathExists(path):
                        removeWorkingPath(path)
                closeRecordingSoftware()
            else:
                 removeWorkingPath(path)
    elif (tmp == "Temp"):
        tmp = True
        work = False
        macroTitle = str(title)
        path = pathlib.Path.cwd()
        path = str(path)
        path = path[:-4]
        path = pathlib.PurePath(path, "myMacros", "tmp", macroTitle)
        path = pathlib.Path(path)
        macroPath = path
        if pathExists(path):
            result2 = ctypes.windll.user32.MessageBoxW(0, "Macro already exists with this title, please choose a new title.","", MB_OK)
        else:
            if launchRecordingSoftware(path, macroTitle):
                if copyScript(path, macroPath, macroTitle, tmp, work):
                    pass
                else:
                    if pathExists(path):
                        removeWorkingPath(path)
                closeRecordingSoftware()
            else:
                 removeWorkingPath(path)
    else:
        tmp = False
        work = False
        macroTitle = str(title)
        path = pathlib.Path.cwd()
        path = str(path)
        path = path[:-4]
        path = pathlib.PurePath(path, "myMacros", "misc", macroTitle)
        path = pathlib.Path(path)
        macroPath = path
        if pathExists(path):
            result2 = ctypes.windll.user32.MessageBoxW(0, "Macro already exists with this title, please choose a new title.","", MB_OK)
        else:
            if launchRecordingSoftware(path, macroTitle):
                if copyScript(path, macroPath, macroTitle, tmp, work):
                    pass
                else:
                    if pathExists(path):
                        removeWorkingPath(path)
                closeRecordingSoftware()
            else:
                 removeWorkingPath(path)
    print("KILL")
    if "AutoHotkey.exe" in (p.name() for p in psutil.process_iter()):
        try:
            os.system("taskkill /im AutoHotKey.exe")
        except Exception:
            print("Couldn't Close Software")
    subprocess.Popen(['C:\Program Files\AutoHotKey\AutoHotkey.exe','rightClickLauncher.ahk'])
if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
