import json

def config():
    with open('settings.json', 'r') as j:
        settings = json.load(j)
    return settings

def modif(name, value):
    settings = config()
    settings[name] = value
    with open("settings.json", "w") as j:
        json.dump(settings, j)
