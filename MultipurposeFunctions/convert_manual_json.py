import sys
import json

from try_catch import try_catch
from write_json import write_json

def convert_to_character(username):

    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"

    with open(inputfile, "r") as f:
        info = f.read()
        weight = int(info[info.find('weight'):].replace('weight ', '').split()[0])
        lTime = int(info[info.find('long time'):].replace('long time ', '').split()[0])
        lDistance = int(info[info.find('long distance'):].replace('long distance ', '').split()[0])
        iq = int(info[info.find('iq'):].replace('iq ', '').split()[0])
        react = int(info[info.find('react time'):].replace('react time ', '').split()[0])
    sTime = find_time(username)
    sDistance = find_distance(username)
    output = {
        'weight' : weight,
        'long time' : lTime,
        'long distance' : lDistance,
        'iq' : iq,
        'reaction time' : react,
        'sprint time'  : sTime,
        'sprint distance' : sDistance
    }
    write_json(output, username)


def find_time(username):
    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"

    f = open(inputfile, "r")
    info = f.read()
    total = 0

    if info.find('hour') != -1:
        hour = info[(info.find(' ', (info.find("hour"))-5, (info.find("hour")))) + 1: (info.find("hour")) - 1]
        hour = try_catch(hour)
        minute = info[(info.find(' ', (info.find("minute"))-5, (info.find("minute")))) + 1: (info.find("minute")) - 1]
        minute = try_catch(minute)
        if info.find('minute') == -1:
            minute = '0'
            minute = int(minute)
        second = info[(info.find(' ', (info.find("second"))-5, (info.find("second")))) + 1: (info.find("second")) - 1]
        second = try_catch(second)
        if info.find('second') == -1:
            second = '0'
            second = int(second)
        total = hour * 3600 + minute * 60 + second

    elif info.find('minute') != -1:
        minute = info[(info.find(' ', (info.find("minute"))-5, (info.find("minute")))) + 1: (info.find("minute")) - 1]
        minute = try_catch(minute)
        second = info[(info.find(' ', (info.find("second"))-5, (info.find("second")))) + 1: (info.find("second")) - 1]
        second = try_catch(second)
        if info.find('second') == -1:
            second = '0'
            second = int(second)
        total = minute * 60 + second

    elif info.find('second') != -1:
        second = info[(info.find(' ', (info.find("second"))-5, (info.find("second")))) + 1: (info.find("second")) - 1]
        second = try_catch(second)
        total = second

    return total


def find_distance(username):
    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"
    f = open(inputfile, "r")
    info = f.read()
    total = 0

    if info.find('kilometer') != -1:
        kilometer = info[(info.find(' ', (info.find("kilometer")) - 5, (info.find("kilometer")))) + 1: (info.find("kilometer")) - 1]
        kilometer = try_catch(kilometer)
        meter = info[(info.find(' ', (info.find("meters."))-5, (info.find("meters.")))) + 1: (info.find("meters.")) - 1]
        meter = try_catch(meter)
        if info.find('meters.') == -1:
            meter = '0'
            meter = int(meter)
        total = kilometer * 1000 + meter

    elif info.find('meter.') != -1:
        meter = info[(info.find(' ', (info.find("meters.")) - 5, (info.find("meters.")))) + 1: (info.find("meters.")) - 1]
        total = meter

    return total