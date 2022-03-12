import os
import manage_settings as ms
from difflib import SequenceMatcher
import webbrowser as wb

DATA = ms.config()

BASE_DIR = DATA['base_dir']
APPS = os.listdir(BASE_DIR)

######################################## CLASS ######################################

class Record:
    def __init__(self, command, key, keys):
        self.command = command
        self.key = key
        self.keys = keys

######################################## FUNCTIONS ##################################

def similar(a, b): # str only
    return (a.lower() == b.lower()) or SequenceMatcher(None, a, b).ratio() >= 0.75

def open_file(data):
    PATH = ''
    for i in range(len(APPS)):
        name = APPS[i].split('.')[0] # app name in desktop
    
        if similar(data.key, name):
            PATH = BASE_DIR + APPS[i]
            print(PATH)
    return PATH

def search_browser(data):
    if data.keys!=[]:
        SITE = data.key
        PARAMS = '+'.join(data.keys)
        if similar(SITE, 'amazon'): 
            search = f'https://www.amazon.com/s?k={PARAMS}'
        else:
            search = f'https://www.{SITE}.com/search?q={PARAMS}'
        
        print(search)
    return search

def exec(record):
    command = record.split()[0]
    key = record.split()[1]
    keys = record.split()[2:] if len(record.split()) else ''
    data = Record(command, key, keys)

    if similar(command, 'ouvre'):
        execute = open_file(data)
        os.startfile(execute)
    elif similar(command, 'cherche'):
        search = search_browser(data)
        wb.open(search) 