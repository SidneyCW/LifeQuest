import sys
import json
sys.path.append('MultipurposeFunctions')

from try_catch import try_catch
from chess_elo import chess_elo_getter

def intelligenceCalc(username):
    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"
    f = open(inputfile, "r")

    userDataJson = open("Saved User Data/user_lvls.json")
    userData = json.load(userDataJson)

    _Data = f.read()
    iq = userData[username]['iq']
    chess_elo = chess_elo_getter(userData[username]["chess.com_username"])
    print(chess_elo)
    chessLvl = chess_elo / 100
    iqLvl = iq / 7.5
    intLvl = round((chessLvl + (iqLvl*2)) / 3)

    return intLvl

intelligenceCalc('Sleepy')