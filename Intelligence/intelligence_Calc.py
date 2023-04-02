import sys

sys.path.append('MultipurposeFunctions')

from try_catch import try_catch

def intelligenceCalc(username):
    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"
    f = open(inputfile, "r")

    chess_elo = f.read()
    iq = chess_elo[((chess_elo.find("iq"))+3): ((chess_elo.find("iq"))+6)]
    chess_elo = chess_elo[((chess_elo.find("elo"))+4): ((chess_elo.find("elo"))+8)]

    chess_elo = try_catch(chess_elo)
    iq = try_catch(iq)

    if type(chess_elo) == '<class str>':
        return round((((chess_elo * 680) / (800 ** 2) * 10) + ((iq ** 2) / (100 ** 2) * 8)) / 2)
    
    return round((iq ** 2) / (100 ** 2) * 8)
