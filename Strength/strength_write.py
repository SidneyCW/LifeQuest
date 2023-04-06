# Importing required modules
import json # Used to work with JSON data
import strong_reader # A custom module for reading data from a CSV file
import sys # Used to modify the system path

# Adding a custom module directory to the system path
sys.path.append('MultipurposeFunctions')

# Importing a custom function from the custom module
from write_json import write_json

# Defining a class for writing user's strength level to a JSON file
class StrengthWrite:
    # Initializing the class with a username
    def __init__(self, username):
        self.username = username
    
    # Defining a method for calculating the user's strength level and writing it to a JSON file
    def writeStrongStr(self):
        # Calculating the user's strength level using data from a CSV file
        strengthLvl = strong_reader.calcAvg("strong - " + self.username + ".csv")
        
        # Creating a dictionary containing the user's strength level
        userData = {
            "strLvl": strengthLvl
        }
        
        # Writing the user's data to a JSON file
        write_json(userData, "Saved User Data/"+ self.username +".json")
        
        # Returning nothing
        return None