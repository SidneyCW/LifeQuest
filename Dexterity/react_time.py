def react_calc(username):
    inputfile = "User Input Data/Manual Input Data/" + username + "_Data.txt"
    with open(inputfile, "r") as f:
            info = f.read()
            reactSpeed = int(info[info.find('react time'):].replace('react time ', '').split()[0])
    lvl = round(30 - (reactSpeed / 12.4))
    return lvl