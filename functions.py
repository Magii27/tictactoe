def akt(input):

    # Trennung von dem Win/Lose/Draw in die Kennzeichnung und der Zahl
    wld = input[input.find(" ") + 1:]
    wldzahl = wld[1:]
    wldk = wld[:1]

    # Zahl wird hochgezählt
    wldzahl = int(wldzahl) + 1

    # Die neue Win/Lose/Draw Kennzeichnung wird zusammengesetzt
    string = wld + str(wldzahl)

    # Der alte Win/Lose/Draw wert wird mit dem neuen ersetzt
    output = input.replace(wldk, string)

    return output
