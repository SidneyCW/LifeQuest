import sys
from agility_calc import agilityCalc
from react_time import react_calc

sys.path.append('MultipurposeFunctions')


def calcDex(username):
    reactSpeed = react_calc(username)
    agilitySpeed = agilityCalc(username)
    dexLvl = round((reactSpeed + (agilitySpeed*3))/4)
    return dexLvl