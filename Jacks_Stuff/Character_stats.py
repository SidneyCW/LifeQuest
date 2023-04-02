import sys

sys.path.append('MultipurposeFunctions')
sys.path.append('Intelligence')
sys.path.append('Dexterity')

import write_json
import try_catch
from Intelligence.intelligenceCalc import intelligenceCalc
from Dexterity.agilityCalc import agilityCalc



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


    userData = {
        "aglLvl": agilityCalc(username),
        "intLvl": intelligenceCalc(username)
    }
    
    write_json.write_json(userData, "Saved User Data/"+ username +".json")

    """
    f = open("valuefile.txt", "w")
    for i in range(len(values)):
        f.write(attributes[i] + " " + values[i] + ' ')
    f.write('\n')
    f.close()
    for i in range(6):
        values[i] = int(values[i])
    """
