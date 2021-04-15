f = open("Daten", "r+")
daten = f.read().splitlines()
ldaten = len(daten)


test = daten[2]
print(test[3:4])
#nächsterzug = string[poszug:poszug + 1]