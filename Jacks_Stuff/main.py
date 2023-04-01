import Character_stats


class Start:
    print('Do you want to input new data? if so enter y')
    answer = input('answer: ')

    if(answer == 'y'):
        Character_stats.add_info()
    print('Do you want to see your levels? if so enter y')
    answer = input('answer: ')
    if(answer == 'y'):
        Character_stats.new_day()

