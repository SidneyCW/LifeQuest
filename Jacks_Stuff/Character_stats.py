import sys

sys.path.append('MultipurposeFunctions')
                
import write_json

time = 0
distance = 0
username = "blaze"
inputfile = "User Input Data/" + username + "Data.txt"


def add_info():

    chess_elo = input("chess elo: ")
    iq = input("iq: ")
    run_time = input("run time: ")
    run_distance = input("run distance: ")

    chess_elo = try_catch(chess_elo)
    iq = try_catch(iq)

    f = open("demofile.txt", "w")
    chess_elo = str(chess_elo)
    iq = str(iq)
    
    f.write("chess elo " + chess_elo)
    f.write('\n')
    f.write("iq " + iq)
    f.write('\n')
    f.write('time ' + run_time)
    f.write('\n')
    f.write('distance ' + run_distance + '.')
    f.close()


def new_day():
    
    level = [0, 0, 0, 0, 0, 0]
    f = open(inputfile, "r")

    chess_elo = f.read()
    iq = chess_elo[((chess_elo.find("iq"))+3): ((chess_elo.find("iq"))+6)]
    chess_elo = chess_elo[((chess_elo.find("elo"))+4): ((chess_elo.find("elo"))+8)]

    chess_elo = try_catch(chess_elo)
    iq = try_catch(iq)

    if type(chess_elo) == '<class str>':
        level[3] = round((((chess_elo * 680) / (800 ** 2) * 10) + ((iq ** 2) / (100 ** 2) * 8)) / 2)
    else:
        level[3] = round((iq ** 2) / (100 ** 2) * 8)

    time = find_time()
    distance = find_distance()

    speed = distance/time

    level[1] = round(((speed)**2) / (5.5 ** 2) * 8)

    attributes = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    values = [0, 0, 0, 0, 0, 0]
    values[3] = level[3]
    values[1] = level[1]

    for i in range(6):
        values[i] = str(values[i])

    for i in range(6):
        print(values[i])
    userData = {
        "aglLvl": int(values[1]),
        "intLvl": int(values[3])
    }
    
    write_json.write_json(userData, "Saved User Data/"+ username +".json")
    f = open("valuefile.txt", "w")
    for i in range(len(values)):
        f.write(attributes[i] + " " + values[i] + ' ')
    f.write('\n')
    f.close()
    for i in range(6):
        values[i] = int(values[i])
    


def try_catch(number):
    if number == ' ':
        pass
    else:
        try:
            number = int(number)

        except TypeError:
            print('Something went wrong')

        except ValueError:
            print('Something went wrong')

    return number


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

new_day()