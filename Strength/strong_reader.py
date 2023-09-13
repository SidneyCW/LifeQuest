import csv
from datetime import date
import json

exercise_type = {
    'Lat Pulldown (Cable)': ['back','bicep'], 
    'Preacher Curl (Barbell)': ['bicep'], 
    'Seated Row (Cable)': ['back'], 
    'Hammer Curl (Dumbbell)': ['bicep'], 
    'Chin Up (Assisted)': ['bicep'], 
    'Incline Bench Press (Dumbbell)': ['chest','tricep','shoulder'], 
    'Triceps Extension (Cable)': ['tricep'], 
    'Lateral Raise (Dumbbell)': ['shoulder'], 
    'Triceps Pushdown (Cable - Straight Bar)': ['tricep'], 
    'Chest Fly': ['chest'], 
    'Bicep Curl (Dumbbell)': ['bicep'], 
    'Reverse Fly (Machine)': ['back'], 
    'T Bar Row': ['back'], 
    'Hip Abductor (Machine)': ['leg'], 
    'Hip Adductor (Machine)': ['leg'], 
    'Stair master ': ['legs'], 
    'Bench Press (Barbell)': ['chest','tricep','shoulder'], 
    'Triceps Dip (Assisted)': ['tricep'], 
    'Sit Up': ['leg'], 
    'Leg Press': ['leg'], 
    'Seated Leg Press (Machine)': ['leg'], 
    'Seated Leg Curl (Machine)': ['leg'], 
    'Leg Extension (Machine)': ['leg'], 
    'Triceps Dip': ['tricep'], 
    'Face Pull (Cable)': ['shoulder'], 
    'Calf Press on Seated Leg Press': ['leg'], 
    'Reverse Curl (Barbell)': ['bicep'], 
    'Incline Bench Press (Barbell)': ['chest','tricep','shoulder'], 
    'Chin Up': ['bicep'], 
    'Chest Press (Machine)': ['chest'], 
    'Iso-Lateral Row (Machine)': ['back'],
    'Squat (Barbell)': ['leg'],
    'Deadlift (Barbell)': ['back','leg']
}
# dictionary of all currently available excercises with their values being the muscle group that the exercise impacts

per_level_data = {
    'Lat Pulldown (Cable)': 10.4, 
    'Preacher Curl (Barbell)': 6.6, 
    'Seated Row (Cable)': 10.8, 
    'Hammer Curl (Dumbbell)': 3.4, 
    'Incline Bench Press (Dumbbell)': 5, 
    'Triceps Extension (Cable)': 7.1, 
    'Lateral Raise (Dumbbell)': 2.6, 
    'Triceps Pushdown (Cable - Straight Bar)': 8.7, 
    'Chest Fly': 12.2, 
    'Bicep Curl (Dumbbell)': 3.8, 
    'Reverse Fly (Machine)': 9.2, 
    'T Bar Row': 12, 
    'Hip Abductor (Machine)': 15.7, 
    'Hip Adductor (Machine)': 17.1, 
    'Stair master ': 1, 
    'Bench Press (Barbell)': 12.4, 
    'Triceps Dip (Assisted)': 1.6, 
    'Sit Up': 5.3, 
    'Leg Press': 31.8, 
    'Seated Leg Press (Machine)': 27.5, 
    'Seated Leg Curl (Machine)': 11.3, 
    'Leg Extension (Machine)': 13.7, 
    'Triceps Dip': 1.6, 
    'Face Pull (Cable)': 7.4, 
    'Calf Press on Seated Leg Press': 34.3, 
    'Reverse Curl (Barbell)': 6.7, 
    'Incline Bench Press (Barbell)': 11, 
    'Chin Up': 0.8, 
    'Chest Press (Machine)': 13, 
    'Iso-Lateral Row (Machine)': 10.8,
    'Squat (Barbell)': 16.1,
    'Deadlift (Barbell)': 18.4
}
# amount of weight or reps increase in order to progress in level

def checkExerExist(username, exercise, one_rep_max):
    if exercise in exercise_type and exercise in per_level_data:
        return None
    else:
        with open('Saved User Data/user_lvls.json', 'r') as user_lvls_file:
            user_lvls = json.load(user_lvls_file)
        muscle_group = str(input(exercise + "\nWhat muscle group does this mostly use?\n(c = chest | bi = biceps | ba = back | t = triceps | l = legs | s = shoulders)\n"))
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

        exercise_type[exercise] = [muscle_group]
        per_level_data[exercise] = per_level

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
    Strong_file_loc = "strong - " + username + ".csv"
    Strong_file = "User Input Data/Strong/" + Strong_file_loc
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

            level = int(round((one_rep_max)/per_level_data[key]))
            Set_date = str(row[0])[:7]
            for group in exercise_type[key]:
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


print(calcStr('Sleepy'))