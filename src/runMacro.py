import subprocess, sys, os, clipboard
def main(path):
    title = os.path.basename(path)
    try:
        title = title+".ahk"
        subprocess.call(['C:\Program Files\AutoHotKey\AutoHotkey.exe',title], cwd=path)
    except rawException:
        title = title+"Raw.ahk"
        subprocess.call(['C:\Program Files\AutoHotKey\AutoHotkey.exe',title], cwd=path)
if __name__ == "__main__":
    main(sys.argv[1])
