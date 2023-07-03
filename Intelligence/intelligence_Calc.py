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
    iq = int(_Data[_Data.find('iq'):].replace('iq ', '').split()[0])
    chess_elo = chess_elo_getter(userData[username]["chess.com_username"])
    chess_elo = try_catch(chess_elo) 
    iq = try_catch(iq)
    chessLvl = chess_elo / 100
    iqLvl = iq / 7.5
    intLvl = round((chessLvl + (iqLvl*2)) / 3)

    return intLvl
#testin shite
