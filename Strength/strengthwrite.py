import json
import strongreader
import write_json
      
class StrengthWrite:
    def __init__(self, username):
        self.username = username
    
    def writeStrongStr(self):
        strengthLvl = strongreader.calcAvg("strong - " + self.username + ".csv")
        userData = {
            "username": self.username,
            "strLvl": strengthLvl
        }
        write_json.write_json(userData, "Saved User Data/"+ self.username +".json")
        return
t1 = StrengthWrite('Blaze')
t1.writeStrongStr()