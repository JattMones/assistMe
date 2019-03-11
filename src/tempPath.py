import subprocess, pathlib, os, time, sys
from distutils.dir_util import copy_tree
def removeWorkingPath(path):
        dir = pathlib.Path(path)
        for item in path.iterdir():
            if item.is_dir():
                removeWorkingPath(item)
            else:
                item.unlink()
        path.rmdir()
def pathExists(path):
    if path.is_dir():
        return True
    else:
        return False
# copy subdirectory example
path = pathlib.Path.cwd()
path = str(path)
path = path[:-4]
path = pathlib.PurePath(path, "myMacros")
fromDirectory = path
path2 = os.environ['Temp']
path2 = pathlib.PurePath(path2, "myMacros")
path2 = pathlib.Path(path2)
if pathExists(path2):
    removeWorkingPath(path2)
time.sleep(5)
path2.mkdir()
path2 = str(path2)
toDirectory = path2
copy_tree(fromDirectory, toDirectory)
print(os.environ['Temp'])
