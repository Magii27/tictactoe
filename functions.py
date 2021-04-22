import random as r


class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def akt(input):

    # Trennung von dem Win/Lose/Draw in die Kennzeichnung und der Zahl
    wld = input[input.find(" ") + 1:]
    wldzahl = wld[1:]
    wldk = wld[:1]
    # Zahl wird hochgezählt
    wldzahl = int(wldzahl) + 1
    # Die neue Win/Lose/Draw Kennzeichnung wird zusammengesetzt
    string = wldk + str(wldzahl)
    # Der alte Win/Lose/Draw wert wird mit dem neuen ersetzt
    output = input.replace(wld, string)
    return output


def isclear(field, input):
    if field[input] == str(input):
        return True
    else:
        print("Das Feld ist belegt")
        return False


def random(field, array_s, input, move):

    nummer = 1
    array = []
    string_array = []
    if input != "":
        for x in array_s:
            if input in x[0:move * 2]:
                string_array.append(x[move*2+3:move*2+4])
                # print("String: ", x)
                # print(string_array)
    for x in field:
        if field[nummer] != (color.BOLD + color.RED + "X" + color.END) and field[nummer] != (color.BOLD + color.BLUE + "O" + color.END) and field[nummer] not in string_array:
            # print("x: ", x)
            array.append(x)
        nummer += 1
    if not array and not string_array:
        output = 1
        return output
    elif not array:
        array = string_array
        output = r.sample(array, k=1)
        return int(output[0])
    else:
        output = r.sample(array, k=1)
        return int(output[0])


def searchandersrum(array, input, move):
    buchstabe = ""
    nummer = 0
    string = ""
    try:
        for x in array:
            if input in x[0:move * 2]:
                if buchstabe == "":
                    buchstabe = x[x.find(" ") + 1:x.find(" ") + 2]
                    zahl = x[x.find(" ") + 2:]
                    string = x
                    posarray = nummer
                elif buchstabe == "L":
                    if x[x.find(" ") + 1:x.find(" ") + 2] == buchstabe:
                        if x[x.find(" ") + 2:] > zahl:
                            zahl = x[x.find(" ") + 2:]
                            string = x
                            posarray = nummer
                elif buchstabe == "D":
                    if x[x.find(" ") + 1: x.find(" ") + 2] == "L":
                        zahl = x[x.find(" ") + 2:]
                        buchstabe = "L"
                        string = x
                        posarray = nummer
                    elif x[x.find(" ") + 1: x.find(" ") + 2] == "D":
                        if x[x.find(" ") + 2:] > zahl:
                            zahl = x[x.find(" ") + 2:]
                            string = x
                            posarray = nummer
                else:
                    if x[x.find(" ") + 1: x.find(" ") + 2] == "L":
                        zahl = x[x.find(" ") + 2:]
                        buchstabe = "L"
                        string = x
                        posarray = nummer
                    elif x[x.find(" ") + 1: x.find(" ") + 2] == "D":
                        zahl = x[x.find(" ") + 2:]
                        buchstabe = "D"
                        string = x
                        posarray = nummer
                    elif x[x.find(" ") + 1: x.find(" ") + 2] == "W":
                        if x[x.find(" ") + 2:] > zahl:
                            zahl = x[x.find(" ") + 2:]
                            string = x
                            posarray = nummer
            nummer += 1
        if string[string.find(" ") + 1: string.find(" ") + 2] == "W" or string == "":
            return False
        else:
            nächsterzug = string[(move + (move - 1)):(move + move)]
            return nächsterzug
    except ValueError:
        return False


def search(array, input, move):
    buchstabe = ""
    nummer = 0
    string = ""
    try:
        for x in array:
            if input in x[0:move*2]:
                if buchstabe == "":
                    buchstabe = x[x.find(" ") + 1:x.find(" ") + 2]
                    zahl = x[x.find(" ") + 2:]
                    string = x
                    posarray = nummer
                elif buchstabe == "W":
                    if x[x.find(" ") + 1:x.find(" ") + 2] == buchstabe:
                        if x[x.find(" ") + 2:] > zahl:
                            zahl = x[x.find(" ") + 2:]
                            string = x
                            posarray = nummer
                elif buchstabe == "D":
                    if x[x.find(" ") + 1: x.find(" ") + 2] == "W":
                        zahl = x[x.find(" ") + 2:]
                        buchstabe = "W"
                        string = x
                        posarray = nummer
                    elif x[x.find(" ") + 1: x.find(" ") + 2] == "D":
                        if x[x.find(" ") + 2:] > zahl:
                            zahl = x[x.find(" ") + 2:]
                            string = x
                            posarray = nummer
                else:
                    if x[x.find(" ") + 1: x.find(" ") + 2] == "W":
                        zahl = x[x.find(" ") + 2:]
                        buchstabe = "W"
                        string = x
                        posarray = nummer
                    elif x[x.find(" ") + 1: x.find(" ") + 2] == "D":
                        zahl = x[x.find(" ") + 2:]
                        buchstabe = "D"
                        string = x
                        posarray = nummer
                    elif x[x.find(" ") + 1: x.find(" ") + 2] == "L":
                        if x[x.find(" ") + 2:] > zahl:
                            zahl = x[x.find(" ") + 2:]
                            string = x
                            posarray = nummer
            nummer += 1
        if string[string.find(" ") + 1: string.find(" ") + 2] == "L" or string == "":
            return False
        else:
            nächsterzug = string[(move + (move - 1)):(move + move)]
            return nächsterzug
    except ValueError:
        return False


def IsWinner(bo, le):

    return ((bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))


def board(field):
    print("\n"),
    print("\t     |     |"),
    print("\t  {}  |  {}  |  {}".format(field[1], field[2], field[3])),
    print('\t_____|_____|_____'),
    print("\t     |     |"),
    print("\t  {}  |  {}  |  {}".format(field[4], field[5], field[6])),
    print('\t_____|_____|_____'),
    print("\t     |     |"),
    print("\t  {}  |  {}  |  {}".format(field[7], field[8], field[9])),
    print("\t     |     |"),
    print("\n")


def zusammenfügen(input, ergebnis):
    output = input + " " + ergebnis + "1"
    return output