import json
import strong_reader
import sys

sys.path.append('MultipurposeFunctions')
                
from write_json import write_json
      
class StrengthWrite:
    def __init__(self, username):
        self.username = username
    
    def writeStrongStr(self):
        strengthLvl = strong_reader.calcAvg("strong - " + self.username + ".csv")
        userData = {
            "strLvl": strengthLvl
        }
        write_json(userData, "Saved User Data/"+ self.username +".json")
        return