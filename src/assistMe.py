from kivy.app import App
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.button import Button
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
import os, sys, clipboard, psutil
import pathlib
import time
import ctypes
from ctypes.wintypes import HWND, LPWSTR, UINT
from recordCleaning import removeWorkingPath, copy_tree, pathExists
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
#Get OS type, and set OS specific commands and dependencies
if (os.name is "posix"):
    import subprocess32 as subprocess
    Posix = True
else:
    Posix = False
    import subprocess
class workPage(GridLayout):
    def __init__(self, **kwargs):
        self.cols =  1
        super(workPage, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.add_widget(Label(text='Quick menu, press Ctrl+q'))
        self.add_widget(Button(text='Make a work recording',on_press = recTitle3, on_release = showMenu,background_color = (1,1,1,1)))
        self.add_widget(Button(text='Back',on_press = showMenu,background_color = (0,0,0,1)))
        Window.size = (175, 175)
Config.set('graphics', 'resizable', False)
def showMenu(self):
    App.get_running_app().stop()
    Macros_Menu().run()
def startScheduler(self):
    subprocess.Popen(['C:\Program Files\AutoHotKey\AutoHotkey.exe','startSchedule.ahk'])
    App.get_running_app().stop()
    Macros_Menu().run()
def showButton(self):
    App.get_running_app().stop()
    AM().run()
def showMyMacros(self):
    App.get_running_app().stop()
    Work_Macros().run()
def showHelp(self):
    App.get_running_app().stop()
    Help_Page().run()
def showRecord(self):
    App.get_running_app().stop()
    Record_Macro().run()
def showError(self):
    App.get_running_app().stop()
    Error_Help().run()
def showTempMacros(self):
    App.get_running_app().stop()
    Temp_Macro().run()
def openHelpFolder(self):
    path = pathlib.Path.cwd()
    path = str(path)
    path = path[:-4]
    path = pathlib.PurePath(path, "help")
    path = str(path)
    if(Posix):
        subprocess.call(["gnome-open",path])
    else:
        subprocess.call(["explorer.exe",path])
def recTitle2(self):
    App.get_running_app().stop()
    Record_Title2().run()
def recTitle3(self):
    App.get_running_app().stop()
    Record_Title3().run()
def recTitle(self):
    App.get_running_app().stop()
    Record_Title().run()
def startRecordClean(self):
    subprocess.call(["python", "recordCleaning.py", "Work", str(textIn)])
def startRecordClean2(self):
    subprocess.call(["python", "recordCleaning.py", "Temp", str(textIn)])
def startRecordClean3(self):
    subprocess.call(["python", "recordCleaning.py", "Misc", str(textIn)])
def on_text(instance, value):
    print('The widget', instance, 'have:', value)
    global textIn
    textIn = str(value)
def writeError(self):
    path = pathlib.Path.cwd()
    path = pathlib.PurePath(path, "errorLog.txt")
    path = pathlib.Path(path)
    if(not(path.exists())):
        data = open(path,"x")
    with open(path, "a") as errorLog:
        errorLog.write("\n"+str(textIn))
def on_request_close(self, *args):
    result2 = ctypes.windll.user32.MessageBoxW(0, "Are you sure you want to exit?","", MB_OKCANCEL)
    try:
        if result2 == IDOK:
            if "AutoHotkey.exe" in (p.name() for p in psutil.process_iter()):
                try:
                    os.system("taskkill /im AutoHotKey.exe")
                except Exception:
                    print("Couldn't Close Software")
            path = os.environ['Temp']
            path = pathlib.PurePath(path, "myMacros")
            path = pathlib.Path(path)
            removeWorkingPath(path)
            path = pathlib.Path.cwd()
            f = open("rightClickLauncher.ahk", "r")
            contents = f.readlines()
            f.close()
            start = None
            stop = None
            for i in range(len(contents)):
                if contents[i] == ";End misc submenu\n":
                    start = i+3
                elif contents[i] == ";End tmp submenu\n":
                    stop = i
            if start != None and stop != None:
                contents = contents[:start] + contents[stop:]
                contents = "".join(contents)
            f = open("rightClickLauncher.ahk", "w+")
            f.write(contents)
            f.close()
            path = str(path)
            path = path[:-4]
            path = pathlib.PurePath(path, "myMacros","tmp")
            path = pathlib.Path(path)
            removeWorkingPath(path)
            path.mkdir()
            return False
        elif result2 == IDCANCEL:
            return True
        else:
            print("Unknown MessageBox return code")
            return True
    except WindowsError as win_err:
        print("An error occurred:\n{}".format(win_err))
        return True

class pressMe(GridLayout):
    def __init__(self, **kwargs):
        super(pressMe, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.cols =  2
        self.add_widget(Button(text='', background_normal = 'logo.jpg', on_press = showMenu))
        Window.size = (100, 100)
class helpPage(GridLayout):
    def __init__(self, **kwargs):
        self.cols =  1
        super(helpPage, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.add_widget(Label(text='HelpPage'))
        self.add_widget(Button(text="HelpFolder",on_press = openHelpFolder, background_color = (1,1,1,1)))
        self.add_widget(Button(text="SendError",on_press = showError,background_color = (1,1,1,1)))
        self.add_widget(Button(text='Back',on_press = showMenu,background_color = (0,0,0,1)))
        Window.size = (175, 175)

class recordPage(GridLayout):
    def __init__(self, **kwargs):
        super(recordPage, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.cols =  1
        self.add_widget(Button(text='Start smart macros', on_press= startScheduler))
        self.add_widget(Button(text='Make a misc recording', on_press = recTitle))
        self.add_widget(Button(text='Back',on_press = showMenu,background_color = (0,0,0,1)))
        Window.size = (175, 175)
class errorPage(GridLayout):
    def __init__(self, **kwargs):
        super(errorPage, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.cols =  2
        usr_input = TextInput(multiline=True, size_hint_x = None, width = 375)
        usr_input.bind(text=on_text)
        self.add_widget(Button(text='Send Error', on_press = writeError, on_release = showMenu))
        self.add_widget(usr_input)
        self.add_widget(Button(text='Help', on_press = showHelp, on_release = showMenu))
        self.add_widget(Button(text='Back',on_press = showMenu,background_color = (0,0,0,1), size_hint_x = None, width = 375))
        Window.size = (500, 175)
class tempPage(GridLayout):
    def __init__(self, **kwargs):
        self.cols =  1
        super(tempPage, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.add_widget(Label(text='Quick menu, press Ctrl+q'))
        self.add_widget(Button(text='Make a tmp recording',on_press = recTitle2, on_release = showMenu,background_color = (1,1,1,1)))
        self.add_widget(Button(text='Back',on_press = showMenu,background_color = (0,0,0,1)))
        Window.size = (175, 175)
class recordTitlePage(GridLayout):
    def __init__(self, **kwargs):
        super(recordTitlePage, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.cols =  2
        usr_input = TextInput(multiline=True, size_hint_x = None, width = 375)
        usr_input.bind(text=on_text)
        self.add_widget(Button(text='Save title', on_press = startRecordClean3))
        self.add_widget(usr_input)
        self.add_widget(Button(text='', on_press = showMenu))
        self.add_widget(Button(text='Back',on_press = showRecord,background_color = (0,0,0,1), size_hint_x = None, width = 375))
        Window.size = (500, 175)
class recordTitlePage2(GridLayout):
    def __init__(self, **kwargs):
        super(recordTitlePage2, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.cols =  2
        usr_input = TextInput(multiline=True, size_hint_x = None, width = 375)
        usr_input.bind(text=on_text)
        self.add_widget(Button(text='Save title', on_press = startRecordClean2))
        self.add_widget(usr_input)
        self.add_widget(Button(text='', on_press = showMenu))
        self.add_widget(Button(text='Back',on_press = showRecord,background_color = (0,0,0,1), size_hint_x = None, width = 375))
        Window.size = (500, 175)
class recordTitlePage3(GridLayout):
    def __init__(self, **kwargs):
        super(recordTitlePage3, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.cols =  2
        usr_input = TextInput(multiline=True, size_hint_x = None, width = 375)
        usr_input.bind(text=on_text)
        self.add_widget(Button(text='Save title', on_press = startRecordClean))
        self.add_widget(usr_input)
        self.add_widget(Button(text='', on_press = showMenu))
        self.add_widget(Button(text='Back',on_press = showRecord,background_color = (0,0,0,1), size_hint_x = None, width = 375))
        Window.size = (500, 175)
class menu(GridLayout):

    def __init__(self, **kwargs):
        super(menu, self).__init__(**kwargs)
        Window.bind(on_request_close = on_request_close)
        self.cols =  3
        self.add_widget(Button(text='', on_press = showButton))
        self.add_widget(Button(text='', background_normal = 'notepad3.jpg', on_press = showMyMacros))
        self.add_widget(Button(text='', on_press = showButton))
        self.add_widget(Button(text='', background_normal = 'tmp.png', on_press = showTempMacros))
        self.add_widget(Button(text='', background_normal = 'logo.jpg', on_press = showError))
        self.add_widget(Button(text='', background_normal = 'recording.jpg', on_press = showRecord))
        self.add_widget(Button(text='', on_press = showButton))
        self.add_widget(Button(text='', background_normal = 'help.jpg', on_press = showHelp))
        self.add_widget(Button(text='', on_press = showButton))
        Window.size = (175, 175)
class AM(App):
    def build(self):
        return pressMe()
class Macros_Menu(App):
    def build(self):
        return menu()
class Work_Macros(App):
    def build(self):
        return workPage()
class Help_Page(App):
    def build(self):
        return helpPage()
class Record_Macro(App):
    def build(self):
        return recordPage()
class Error_Help(App):
    def build(self):
        return errorPage()
class Temp_Macro(App):
    def build(self):
        return tempPage()
class Record_Title(App):
    def build(self):
        return recordTitlePage()
class Record_Title2(App):
    def build(self):
        return recordTitlePage2()
class Record_Title3(App):
    def build(self):
        return recordTitlePage3()
def Main():
    path2 = os.environ['Temp']
    path2 = pathlib.PurePath(path2, "myMacros")
    path2 = pathlib.Path(path2)
    if pathExists(path2):
        removeWorkingPath(path2)
    path2.mkdir()
    path2 = str(path2)
    toDirectory = path2
    path = pathlib.Path.cwd()
    path = str(path)
    path = path[:-4]
    path = pathlib.PurePath(path, "myMacros")
    fromDirectory = str(path)
    copy_tree(fromDirectory, toDirectory)
    subprocess.Popen(['C:\Program Files\AutoHotKey\AutoHotkey.exe','rightClickLauncher.ahk'])
    AM().run()

if __name__ == "__main__":
    Main()
