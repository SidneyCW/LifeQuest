import sys

sys.path.append('MultipurposeFunctions')

import try_catch

username = ""
inputfile = "User Input Data/" + username + "Data.txt"

def agilityCalc(user):
    username = user    
    time = find_time()
    distance = find_distance()

    speed = distance/time

    return round(((speed)**2) / (5.5 ** 2) * 8)

def find_time():
    

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

def find_distance():
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