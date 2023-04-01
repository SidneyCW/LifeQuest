import json
import strongreader
import sys

sys.path.append('MultipurposeFunctions')
                
import write_json
      
class StrengthWrite:
    def __init__(self, username):
        self.username = username
    
    def writeStrongStr(self):
        strengthLvl = strongreader.calcAvg("strong - " + self.username + ".csv")
        userData = {
            "strLvl": strengthLvl
        }
        write_json.write_json(userData, "Saved User Data/"+ self.username +".json")
        return
t1 = StrengthWrite('Blaze')
t1.writeStrongStr()