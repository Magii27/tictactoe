import functions as fun
update = {"Win": 0, "Lose": 0, "Draw": 0}

for z in range(20000):

    f = open("Daten", "r+")
    fa = open("Daten", "a+")
    daten = f.read().splitlines()
    ldaten = len(daten)

    feld = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
    feldd = feld

    CurrentP = fun.color.BOLD + fun.color.RED + "X" + fun.color.END

    string2 = ""
    stimmt = 0
    speicher = True
    speicher1 = True
    move = 1
    bot = ""
    while True:
        try:
            if move < 10:
                zugbot = fun.random(feldd, daten, bot, move)

                feldd[zugbot] = CurrentP

                bot = bot + "P" + str(zugbot)

            if fun.IsWinner(feldd, CurrentP) is True:
                ergebnis = "L"
                string1 = bot + " " + ergebnis + "1"
                string2 = bot + " " + "W" + "1"
                update["Win"] = update["Win"] + 1
                # print("feldd: 1 ", fun.board(feldd))
                # print(fun.color.BOLD + fun.color.GREEN + "Computer 1 (andersrum) won!" + fun.color.END)
                break

            if CurrentP == fun.color.BOLD + fun.color.RED + "X" + fun.color.END:
                CurrentP = fun.color.BOLD + fun.color.BLUE + "O" + fun.color.END
                CurrentPi = "O"
            else:
                CurrentP = fun.color.BOLD + fun.color.RED + "X" + fun.color.END
                CurrentP1 = "X"

            move += 1
            if move < 10:
                zugbot = fun.random(feldd, daten, bot, move)

                feldd[zugbot] = CurrentP

                bot = bot + "C" + str(zugbot)

                # print("feldd: 1", fun.board(feldd))

                if fun.IsWinner(feldd, CurrentP) is True:
                    ergebnis = "W"
                    string1 = bot + " " + ergebnis + "1"
                    string2 = bot + " " + "L" + "1"
                    update["Lose"] = update["Lose"] + 1
                    # print(fun.color.BOLD + fun.color.GREEN + "The computer2 won!" + fun.color.END)
                    break

                if CurrentP == fun.color.BOLD + fun.color.RED + "X" + fun.color.END:
                    CurrentP = fun.color.BOLD + fun.color.BLUE + "O" + fun.color.END
                else:
                    CurrentP = fun.color.BOLD + fun.color.RED + "X" + fun.color.END

                move += 1
                if move == 10:
                    break
            else:
                # print("feldd: 1", fun.board(feldd))
                ergebnis = "D"
                string1 = bot + " " + ergebnis + "1"
                update["Draw"] = update["Draw"] + 1
                # print("Gleichstand!")
                break
        except KeyError:
            test = 0
            # print("Bitte gib eine numerische Zahl ein")
    # print("spiel: ", z)

    if z % 100 == 0:
        print("Runde: ", z, update)
    # Für das Ergebnis, um es in die Datei einzufügen
    nummer = 0
    for x in daten:

        # Wenn bereits dieses Spiel gelaufen ist, wird der Win, Lose oder Draw hochgezählt
        if bot in x:
            # print("ich bin hier")
            test1 = fun.akt(daten[nummer])
            daten[nummer] = test1

            # Die Daten werden alle gelöscht
            f.truncate(0)
            f.seek(0)

            # Die vorherigen Daten in der variable werden wieder in die Datei geschrieben
            for y in daten:
                f.write(y + "\n")
            stimmt = 1

        nummer += 1

    # Ergebnis in die Datenbank hinzufügen
    if stimmt != 1:
        # string = bot + " " + ergebnis + "1"
        fa.write(string1 + "\n")
        # if string2 != "":
            # fa.write(string2 + "\n")
    f.close()
    fa.close()
