import subprocess, sys, colorama
from termcolor import *
passCount = 0
colorama.init()

def main():
    if len(sys.argv) == 1:
        print(colored("\nStart:", 'blue'), "dependenciesTesting.py")
        subprocess.call(['python', 'checkDependencies\\dependenciesTesting.py'])
        #print("\nStart: guiTesting.py")
        #subprocess.call(['python', 'gui\\guiTesting.py'])
        print(colored("\nStart:", 'blue'), "recordTesting.py")
        subprocess.call(['python', 'recording\\recordTesting.py'])
        #print("\nStart: recoring-cleaning.py")
        #subprocess.call(['python', 'recording-cleaning\\'])
        cprint("\nTest Complete.", 'blue')
    elif len(sys.argv) == 2:
        if sys.argv[1] == "-dependenciesTesting":
            print(colored("\nStart:", 'blue'), "dependenciesTesting.py")
            subprocess.call(['python', 'checkDependencies\\dependenciesTesting.py'])
        #elif sys.argv[1] == "-guiTesting":
        #    subprocess.call(['python', 'checkDependencies2.py'])
        elif sys.argv[1] == "-recordTesting":
            print(colored("\nStart:", 'blue'), "recordTesting.py")
            subprocess.call(['python', 'recording\\recordTesting.py'])
        else:
            print("No such dependency test")
    else:
        print("No such dependency test")
if __name__ == "__main__":
    main()
