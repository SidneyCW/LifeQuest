import sys 
import json

from energy_endurance import calcLvlEnergy
from run_distance_endurance import calcLvlRD
from run_distance_wspeed_endurance import calcLvlRDS
from convert_manual_json import convert_to_character

sys.path.append('MultipurposeFunctions')

from write_json import write_json

def writeEnduranceCon(username):
    endurance = []
    convert_to_character(username)

    userDataJson = open("Saved User Data/user_lvls.json")
    userData = json.load(userDataJson)
    weight = userData[username]['weight']
    distance = userData[username]['long distance']
    time = userData[username]['long time']
    if weight != 0 and time != 0 and distance != 0:
        endurance.append(calcLvlEnergy(weight,time,(distance/time)))
    endurance.append(calcLvlRD(distance))
    level = round(sum(endurance)/len(endurance))
    return level
