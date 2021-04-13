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
        test1 = arraystr[arraystr.find("W")+1:arraystr.find("W")+2]
        #print(test1)
        wl = arraystr[arraystr.find("W"):arraystr.find("W")+4]
        winzahl = int(wl[1:2])
        losezahl= int(wl[3:4])
        winzahl += 1
        losezahl += 1
        string = "W" + str(winzahl) + "L" + str(losezahl)
        wl = wl.replace(wl, string)
        arraystr = arraystr.replace(arraystr[arraystr.find("W"):], wl)
        daten[nummer] = arraystr
        f.truncate(0)
        f.seek(0)
        for y in daten:
            f.write(y+"\n")


        #print("hey", winzahl, losezahl)
        #print("arraystr: ", arraystr)
        #print(test[nummer])

    nummer += 1

#Für das Ergebnis, um es in die Datei einzufügen
for x in daten:

    #Wenn bereits dieses Spiel gelaufen ist, ob gewonnen oder verloren wurde
    if testdaten in x:

        #aktueller string wird umgeschrieben in eine variable
        arraystr = daten[nummer]

        #Trennung von dem Win/Lose und aufteilung in eigene variablen
        wl = arraystr[arraystr.find("W"):arraystr.find("W")+4]
        winzahl = int(wl[1:2])
        losezahl= int(wl[3:4])

        #Abfrage des Ergebnisses
        if ergebnis == "w":
            winzahl += 1
        else:
            losezahl += 1

        #Der neue Win/Lose wird wieder zusammengebunden in einen String
        string = "W" + str(winzahl) + "L" + str(losezahl)

        #Der alte Win/Lose wird mit dem neuen ersetzt und der Array wird mit dem Datensatz aktualisiert
        wl = wl.replace(wl, string)
        arraystr = arraystr.replace(arraystr[arraystr.find("W"):], wl)
        daten[nummer] = arraystr

        #Die Daten werden alle gelöscht
        f.truncate(0)
        f.seek(0)

        #Die alten Daten in der variable werden wieder in die Datei geschrieben
        for y in daten:
            f.write(y+"\n")

    #wenn das Spiel das Erste mal Auftritt
    else:
        if ergebnis == "w":
            winzahl = 1
            losezahl = 0
        else:
            losezahl = 1
            winzahl = 0

        string = testdaten + "W" + str(winzahl) + "L" + str(losezahl)
        daten.append(string)

