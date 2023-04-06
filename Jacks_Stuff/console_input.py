import json
import character_stats as Character_stats


class Start:
    username = input("username: ")
    print('Do you want to input new data? if so enter y')
    answer = input('answer: ')

    if(answer == 'y'):
        Character_stats.change_data(username)
        Character_stats.add_stats(username)
    print('Do you want to see your levels? if so enter y')
    answer = input('answer: ')
    if(answer == 'y'):
        f = open ('Saved User Data/'+ username + '.json')
        data = json.load(f)
        for item in data["user_details"]:
            print(item,":", data["user_details"][item])

