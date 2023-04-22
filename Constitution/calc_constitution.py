
from energy_endurance import calcLvlEnergy
from run_distance_endurance import calcLvlRD
from run_distance_wspeed_endurance import calcLvlRDS
import sys

sys.path.append('MultipurposeFunctions')

from write_json import write_json

    

def writeEnduranceCon(username):
    endurance = []
    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"
    with open(inputfile, "r") as f:
        info = f.read()
        weight = int(info[info.find('weight'):].replace('weight ', '').split()[0])
        time = int(info[info.find('long time'):].replace('long time ', '').split()[0])
        distance = int(info[info.find('long distance'):].replace('long distance ', '').split()[0])
    if weight != 0 and time != 0 and distance != 0:
        endurance.append(calcLvlEnergy(weight,time,(distance/time)))
    endurance.append(calcLvlRD(distance))
    level = round(sum(endurance)/len(endurance))
    return level

