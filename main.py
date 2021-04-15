f = open("Daten", "r+")
daten = f.read().splitlines()
ldaten = len(daten)
print(test)

testdaten = input("gibt mir was: ")

nummer = 0

for x in daten:

    if teilergebnis in x[0:zug]:

    if testdaten in x:
        print(testdaten)
        arraystr = daten[nummer]
        test1 = arraystr[arraystr.find("W") + 1:arraystr.find("W") + 2]
        # print(test1)
        wl = arraystr[arraystr.find("W"):arraystr.find("W") + 4]
        winzahl = int(wl[1:2])
        losezahl = int(wl[3:4])
        winzahl += 1
        losezahl += 1
        string = "W" + str(winzahl) + "L" + str(losezahl)
        wl = wl.replace(wl, string)
        arraystr = arraystr.replace(arraystr[arraystr.find("W"):], wl)
        daten[nummer] = arraystr
        f.truncate(0)
        f.seek(0)
        for y in daten:
            f.write(y + "\n")

        # print("hey", winzahl, losezahl)
        # print("arraystr: ", arraystr)
        # print(test[nummer])

    nummer += 1

# Für das Ergebnis, um es in die Datei einzufügen
nummer = 0
for x in daten:

    # Wenn bereits dieses Spiel gelaufen ist, wird der Win, Lose oder Draw hochgezählt
    if testdaten in x:

        test1 = f.akt(daten[nummer])
        daten[nummer] = test1

        # Die Daten werden alle gelöscht
        f.truncate(0)
        f.seek(0)

        # Die vorherigen Daten in der variable werden wieder in die Datei geschrieben
        for y in daten:
            f.write(y + "\n")

    nummer += 1


