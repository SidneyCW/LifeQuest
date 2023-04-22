# Importing required modules
import json # Used to work with JSON data
import strong_reader # A custom module for reading data from a CSV file
import sys # Used to modify the system path

# Adding a custom module directory to the system path
sys.path.append('MultipurposeFunctions')

# Importing a custom function from the custom module
from write_json import write_json
# Defining a method for calculating the user's strength level and writing it to a JSON file
def writeStrongStr(username):
    # Calculating the user's strength level using data from a CSV file
    strengthLvl = strong_reader.calcStr("strong - " + username + ".csv")
    return strengthLvl