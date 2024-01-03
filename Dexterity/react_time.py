import json

def react_calc(username):
    userDataJson = open("Saved User Data/user_lvls.json")
    userData = json.load(userDataJson)
    reactSpeed = userData[username]['reaction time']
    lvl = round(30 - (reactSpeed / 12.4))
    return lvl