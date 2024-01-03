import sys
import json 

sys.path.append('MultipurposeFunctions')

from try_catch import try_catch
from react_time import react_calc
from convert_manual_json import convert_to_character


def agilityCalc(username):  

    convert_to_character(username)

    userDataJson = open("Saved User Data/user_lvls.json")
    userData = json.load(userDataJson)

    time = userData[username]['sprint time']
    distance = userData[username]['sprint distance']

    speed = round(((distance/time)**2) / (5.5 ** 2) * 8)

    return speed
print(agilityCalc('Blaze'))