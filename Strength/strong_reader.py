import csv
import sys
from datetime import date
import json

sys.path.append('MultipurposeFunctions')

from write_json import write_json

def checkExerExist(username, exercise, one_rep_max):
    exercise_type_json = open('Strength/exercise_type.json')
    exercise_type = json.load(exercise_type_json)
    if exercise in exercise_type['strong']:
        return None
    else:
        with open('Saved User Data/user_lvls.json', 'r') as user_lvls_file:
            user_lvls = json.load(user_lvls_file)
        muscle_group = str(input(exercise + "\nWhat muscle group does this mostly use?\n(c = chest | bi = biceps | ba = back | t = triceps | l = leg | s = shoulders)\n"))
        in_conversion = {
            'c':'chest',
            'bi':'bicep',
            'ba':'back',
            't':'tricep',
            'l':'leg',
            's':'shoulder'
        }
        muscle_group = in_conversion[muscle_group]
        level = user_lvls[username]['strLvl']
        per_level = one_rep_max/level

        new_exercise = {
            exercise : [[muscle_group],per_level]
        }
        write_json(new_exercise, 'strong', 'Strength/exercise_type.json')

        error = {
            'username' : username,
            'type' : 'excercise not in catalogue',
            'excercise' : exercise
        }

        with open('Saved User Data/errors.json', 'r') as error_file:
            error_json = json.load(error_file)
            error_json['Strong_reader'][str(date.today())] = error
    return None


def calcStr(username):
    userDataJson = open("Saved User Data/user_lvls.json")
    userData = json.load(userDataJson)
    exercise_type_json = open('Strength/exercise_type.json')
    exercise_type = json.load(exercise_type_json)
    Strong_file_loc = "strong - " + username + ".csv"
    Strong_file = "User Input Data/Strong/" + Strong_file_loc
    user_weight = userData[username]['weight']
    TODAY = '2023-03' # str(date.today())[:7]
    MONTH = int(TODAY[-2:])
    Prev_month = ''
    if MONTH < 10:
        Prev_month = TODAY[:5] + '0' + str(MONTH-1)
    else:
        Prev_month = TODAY[:5] + str(MONTH-1)
    Prev_month_access = {
        'chest':False,
        'bicep':False,
        'back':False,
        'tricep':False,
        'leg':False,
        'shoulder':False
    }
    month_access = {
        'chest':False,
        'bicep':False,
        'back':False,
        'tricep':False,
        'leg':False,
        'shoulder':False
    }

    muscles = {
        'chest':{'':[1]},
        'bicep':{'':[1]},
        'back':{'':[1]},
        'tricep':{'':[1]},
        'leg':{'':[1]},
        'shoulder':{'':[1]}
    }
    # dictionary of all muscle groups with their values being lists of the last three levels for each muscle group
    with open(Strong_file, 'r') as csvfile:

        reader = csv.reader(csvfile)
        next(reader)
        rows = list(reader)

        for row in rows:
            key = row[3]
            weight = float(row[5])
            reps = float(row[6])
            one_rep_max = weight * (1 + reps/30)

            checkExerExist(username, key, one_rep_max)
            
            exercise_type_json = open('Strength/exercise_type.json')
            exercise_type = json.load(exercise_type_json)
            if key not in ['Chin Up (Assisted)','Stair master','Chin Up']:
                level = int(round((one_rep_max)/exercise_type['strong'][key][1]))
            elif key == 'Chin Up (Assisted)':
                level = int(((user_weight - weight)*(1+ reps/30))/12)
            elif key == 'Stair master':
                level = userData[username]['conLvl']
            elif key == 'Chin Up':
                level = int((user_weight *(1 + reps/30))/12)
            else:
                level = userData[username]['strLvl']

            Set_date = str(row[0])[:7]

            for group in exercise_type['strong'][key][0]:
                if Set_date == Prev_month:
                    Prev_month_access[group] = True
                if Set_date == TODAY:
                    month_access[group] = True
                if Set_date in muscles[group]:
                    muscles[group][Set_date].append(level)
                else:
                    muscles[group][Set_date] = [level]


    with open('Saved User Data/user_lvls.json', 'r') as user_lvls_file:
        user_lvls = json.load(user_lvls_file)

    Group_lvl_list = []
    for group in muscles:
        Group_list = []
        if Prev_month_access[group]:
            Group_list.extend(muscles[group].get(Prev_month, []))
        if month_access[group]:
            Group_list.extend(muscles[group].get(TODAY, []))
        if not month_access[group] and not Prev_month_access[group]:
            Group_list.append(int(user_lvls[username]['strLvl']) - 1)

        Group_lvl = sum(Group_list) / len(Group_list)
        Group_lvl_list.append(Group_lvl)

    Avg = round(sum(Group_lvl_list) / len(Group_lvl_list))
    print(Group_lvl_list)
    return Avg