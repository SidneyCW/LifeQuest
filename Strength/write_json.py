import json

def write_json(new_data, filename):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data["user_details"].update(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        
        
# code written by aman neekhara and found on https://www.geeksforgeeks.org/append-to-json-file-using-python/