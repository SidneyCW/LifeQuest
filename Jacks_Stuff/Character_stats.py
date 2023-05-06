import sys

sys.path.append('MultipurposeFunctions')
sys.path.append('Intelligence')
sys.path.append('Dexterity')
sys.path.append('Strength')
sys.path.append('Constitution')

from agility_Calc import agilityCalc
from intelligence_Calc import intelligenceCalc
from try_catch import try_catch
from write_json import write_json
from dex_write import calcDex
from strong_reader import calcStr
from calc_constitution import writeEnduranceCon
from chess_elo import chess_elo_getter



def write_data(username):
    iq = input("iq: ")
    run_time = input("run time: ")
    run_distance = input("run distance: ")

    chess_elo = try_catch(chess_elo)
    iq = try_catch(iq)

    f = open("User Input Data/Manual Input Data/" + username + "_Data.txt", "w")
    chess_elo = chess_elo_getter(username)
    iq = str(iq)
    
    f.write("chess elo " + chess_elo)
    f.write('\n')
    f.write("iq " + iq)
    f.write('\n')
    f.write('time ' + run_time)
    f.write('\n')
    f.write('distance ' + run_distance + '.')
    f.close()

def replace_data(username, data_type, data = None):
    if data_type == "chess elo":
        chesscom_username = input("chess.com username: ")
        data = chess_elo_getter(chesscom_username)
        print(data)
    with open(f"User Input Data/Manual Input Data/{username}_Data.txt", "r+") as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if data_type in line:
                line = f"{data_type} {data}\n"
            f.write(line)
        f.truncate()
    return None
        

def add_stats(username):
    userData = {
        "dexLvl": calcDex(username),
        "intLvl": intelligenceCalc(username),
        "strLvl": calcStr(username),
        "conLvl": writeEnduranceCon(username)
    }
    
    write_json(userData, username)
    
    return None
add_stats("Blaze")