import csv
import pandas as pd

exercise_type = {
    'Lat Pulldown (Cable)': ['back','bicep'], 
    'Preacher Curl (Barbell)': ['bicep'], 
    'Seated Row (Cable)': ['back'], 
    'Hammer Curl (Dumbbell)': ['bicep'], 
    'Chin Up (Assisted)': ['abs'], 
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
    'Stair master ': ['cardio'], 
    'Bench Press (Barbell)': ['chest','tricep','shoulder'], 
    'Triceps Dip (Assisted)': ['tricep'], 
    'Sit Up': ['abs'], 
    'Leg Press': ['leg'], 
    'Seated Leg Press (Machine)': ['leg'], 
    'Seated Leg Curl (Machine)': ['leg'], 
    'Leg Extension (Machine)': ['leg'], 
    'Triceps Dip': ['tricep'], 
    'Face Pull (Cable)': ['shoulder'], 
    'Calf Press on Seated Leg Press': ['leg'], 
    'Reverse Curl (Barbell)': ['bicep'], 
    'Incline Bench Press (Barbell)': ['chest','tricep','shoulder'], 
    'Chin Up': ['abs'], 
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
    'Chin Up (Assisted)': 1.7, 
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
    'Chin Up': 1.7, 
    'Chest Press (Machine)': 13, 
    'Iso-Lateral Row (Machine)': 10.8,
    'Squat (Barbell)': 16.1,
    'Deadlift (Barbell)': 18.4
}
# amount of weight or reps increase in order to progress in level

def calcAvg(Strong_file_loc):
    Strong_file = "User Input Data/Strong/" + Strong_file_loc
    muscles = {
        'chest':[1],
        'bicep':[1],
        'back':[1],
        'tricep':[1],
        'leg':[1],
        'shoulder':[1],
        'cardio':[1],
        'abs':[1]
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
            level = round((weight * (1 + reps/30))/per_level_data[key])
            for group in exercise_type[key]:
                muscles[group].append(level)
    # Calculate the average level based on the last three levels for each muscle group (stored in the lists within the 'muscles' dictionary), rounding to the nearest integer, and assigning it to the variable 'Avg'
    Avg = round(sum(muscles['chest'][-3:] + muscles['bicep'][-3:] + muscles['back'][-3:] + muscles['tricep'][-3:] + muscles['leg'][-3:] + muscles['shoulder'][-3:]) / 18)
    # Return the calculated average level
    return Avg
