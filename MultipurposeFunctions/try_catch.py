def try_catch(number):
    if number == ' ':
        pass
    else:
        try:
            number = int(number)

        except TypeError:
            print('Something went wrong')

        except ValueError:
            print('Something went wrong')

    return number