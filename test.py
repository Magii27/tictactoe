f = open("Daten", "r+")
daten = f.read().splitlines()
ldaten = len(daten)

test = daten[2]
test1 = test[test.find(" ")+1:]
print(test1[:1])
