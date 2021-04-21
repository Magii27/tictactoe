import functions as fun

f = open("Daten", "r+")
daten = f.read().splitlines()
ldaten = len(daten)

feld = {1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
feldd = feld

# print(color.BOLD + 'Hello World !' + color.END)
while True:
    CurrentP = input("Welcher spieler möchtest du sein? (O / X): ")
    if CurrentP == "X" or CurrentP == "x":
        CurrentP = fun.color.BOLD + fun.color.RED + "X" + fun.color.END
        CurrentPi = "X"
        break
    elif CurrentP == "O" or CurrentP == "o":
        CurrentP = fun.color.BOLD + fun.color.BLUE + "O" + fun.color.END
        CurrentPi = "O"
        break
    else:
        print("Bitte such dir einen Spieler aus")

print(fun.board(feldd))

speicher = True
move = 1
bot = ""
while True:
    try:
        while True:
            eingabe = int(input("Dein Zug: "))
            if fun.isclear(feldd, eingabe) is not True:
                True
            else:
                feldd[eingabe] = CurrentP
                print("Spieler eingabe: ", eingabe)
                bot = bot + "P" + str(eingabe)
                print("bot: " + bot)
                break

        if fun.IsWinner(feldd, CurrentP) is True:
            ergebnis = "L"
            print("feldd: 1 ", fun.board(feldd))
            print(fun.color.BOLD + fun.color.GREEN + "You've won!" + fun.color.END)
            break

        if CurrentP == fun.color.BOLD + fun.color.RED + "X" + fun.color.END:
            CurrentP = fun.color.BOLD + fun.color.BLUE + "O" + fun.color.END
            CurrentPi = "O"
        else:
            CurrentP = fun.color.BOLD + fun.color.RED + "X" + fun.color.END
            CurrentP1 = "X"

        move += 1
        if move < 10:
            if speicher is not False:
                if fun.search(daten, bot, move) is False:
                    speicher = False
                    zugbot = fun.random(feldd)
                else:
                    zugbot = int(fun.search(daten, bot, move))
            else:
                zugbot = fun.random(feldd)

            feldd[zugbot] = CurrentP

            bot = bot + "C" + str(zugbot)

            print("feldd: 1", fun.board(feldd))

            if fun.IsWinner(feldd, CurrentP) is True:
                ergebnis = "W"
                print(fun.color.BOLD + fun.color.GREEN + "The computer won!" + fun.color.END)
                break

            if CurrentP == fun.color.BOLD + fun.color.RED + "X" + fun.color.END:
                CurrentP = fun.color.BOLD + fun.color.BLUE + "O" + fun.color.END
            else:
                CurrentP = fun.color.BOLD + fun.color.RED + "X" + fun.color.END

            move += 1
            if move == 10:
                break
        else:
            print("feldd: 1", fun.board(feldd))
            ergebnis = "D"
            print("Gleichstand!")
            break

    except KeyError:
        print("Bitte gib eine numerische Zahl ein")

# Für das Ergebnis, um es in die Datei einzufügen
nummer = 0
for x in daten:

    # Wenn bereits dieses Spiel gelaufen ist, wird der Win, Lose oder Draw hochgezählt
    if bot in x:
        print("ich bin hier")
        test1 = fun.akt(daten[nummer])
        daten[nummer] = test1

        # Die Daten werden alle gelöscht
        f.truncate(0)
        f.seek(0)

        # Die vorherigen Daten in der variable werden wieder in die Datei geschrieben
        for y in daten:
            f.write(y + "\n")

    nummer += 1

# Ergebnis in die Datenbank hinzufügen
append an file using