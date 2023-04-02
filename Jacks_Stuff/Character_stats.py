import sys

sys.path.append('MultipurposeFunctions')
sys.path.append('Intelligence')
sys.path.append('Dexterity')

from agility_Calc import agilityCalc
from intelligence_Calc import intelligenceCalc
from try_catch import try_catch
from write_json import write_json



def change_data(username):
    chess_elo = input("chess elo: ")
    iq = input("iq: ")
    run_time = input("run time: ")
    run_distance = input("run distance: ")

    chess_elo = try_catch(chess_elo)
    iq = try_catch(iq)

    f = open("User Input Data/Manual Input Data/" + username + "_Data.txt", "w")
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
    

def add_stats(username):
    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"

    userData = {
        "aglLvl": agilityCalc(username),
        "intLvl": intelligenceCalc(username)
    }
    
    write_json(userData, "Saved User Data/"+ username +".json")
