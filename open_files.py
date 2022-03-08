from importlib.resources import path
import os
import subprocess
from difflib import SequenceMatcher

FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
BASE_DIR = 'C:/Users/nahar/Desktop/'
APPS = os.listdir(BASE_DIR)

######################################## FUNCTIONS ##################################

def explore(path): 
    """ Open a file or directory from path in explorer """
    # explorer would choke on forward slashes
    path = os.path.normpath(path)

    if os.path.isdir(path):
        subprocess.run([FILEBROWSER_PATH, path])
    elif os.path.isfile(path):
        subprocess.run([FILEBROWSER_PATH, '/select,', path])


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    PATH = ''

    with open("record.txt", 'r', encoding="utf-8") as f:
        h = f.readline()
        command = h.split()[0]
        app = h.split()[1]

    for i in range(len(APPS)):
        if len(APPS[i].split('.')) >= 2:
            file_type = APPS[i].split('.')[1]
        else : 
            file_type = 'dir'
        name = APPS[i].split('.')[0]
        
        if (app.lower() == name.lower()) or (similar(app, name)>= 0.75):
            if file_type != 'dir':
                PATH = BASE_DIR + APPS[i]
                print(PATH)
    return PATH

def exec():
    execute = main()
    os.startfile(execute)