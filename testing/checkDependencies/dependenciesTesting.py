import sys, pathlib, os, time, colorama
from termcolor import *
#FileExist method, used to check that the recordingLanguage and recordingSoftware are downloaded on your device
colorama.init()
def applicationFilesExists(app):
        returnStatement = False
        dir_path = 'C:\\'
        for root, dirs, files in os.walk(dir_path):
            for file in files:
                if file.endswith(app):
                    #print(root+'\\'+str(file))
                    returnStatement = True
                    break
            if(returnStatement):
                return True
        else:
            return False

def checkCurrenttPython3():
    if sys.version_info[0] < 3:
        raise Exception("Must be using Python 3")
        return False
    else:
        return True
def checkGUIdependencies():
    try:
        import kivy
        time.sleep(3)
        return True
    except Exception:
        if Posix:
            print("Kivy failed to launch, preparing to install kivy dependencies...")
        else:
            print("Kivy failed to launch, preparing to install kivy dependencies...")
            subprocess.call(["python", "-m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew"])
            subprocess.call(["python", "-m pip install kivy.deps.gstreamer"])
        return False
#Dynamic Dependencies Include recordingLanguage and recordingSoftware
recordingLanguage = "AutoHotkey.exe"
recordingSoftware = "MacroCreator.exe"
def main():
    if len(sys.argv) == 1:
        print("Python3Usage: ", checkCurrenttPython3())
        print("GUIDependencies: ", checkGUIdependencies())
        print("recordingLanguage: ", applicationFilesExists(recordingLanguage))
        print("recordingSoftware: ", applicationFilesExists(recordingSoftware))
        if(checkCurrenttPython3(),checkGUIdependencies(),applicationFilesExists(recordingLanguage),applicationFilesExists(recordingSoftware)):
            print("-------------")
            print(colored("PASS",'green'), __file__)
        else:
            print("-------------")
            print(colored("FAIL", 'red'),  __file__)
            if not(checkCurrenttPython3()):
                print("X checkCurrenttPython3")
            if not(checkGUIdependencies()):
                print("X checkGUIdependencies")
            if not(applicationFilesExists(recordingLanguage)):
                print("X checkRecordingLanguage")
            if not(applicationFilesExists(recordingSoftware)):
                print("X checkRecordingSoftware")
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-Python3Usage":
            print("Python3Usage: ", checkCurrenttPython3())
        elif sys.argv[1] == "-GUIDependencies":
            subprocess.call(['python', 'checkDependencies2.py'])
        elif sys.argv[1] == "-applicationFilesExists":
            print("recordingLanguage: ", applicationFilesExists(recordingLanguage))
            print("recordingSoftware: ", applicationFilesExists(recordingSoftware))
        else:
            print("No such dependency test")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-applicationFilesExists":
            print(sys.argv[2], applicationFilesExists(sys.argv[2]))
        else:
            print("No such depencency test")
    else:
        print("No such dependency test")
if __name__ == "__main__":
    main()
