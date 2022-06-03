import json

def config():
    with open('settings.json', 'r') as j:
        settings = json.load(j)
    return settings

def modif(path, value):
    settings = config()

    if len(path)==1:
        settings[path[0]] = value
    elif len(path)==2:
        settings[path[0]][path[1]] = value
    elif len(path)==3:
        settings[path[0]][path[1]][path[2]] = value
    elif len(path)==4:
        settings[path[0]][path[1]][path[2]][path[3]] = value
    elif len(path)==5:
        settings[path[0]][path[1]][path[2]][path[3]][path[4]] = value
    else:
        print('Path Error, number of variable not find in settings.json')

    # settings[name] = value
    with open('settings.json', "w") as j:
        json.dump(settings, j)
