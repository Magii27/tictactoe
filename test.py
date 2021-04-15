import functions as f
f = open("Daten", "r+")
daten = f.read().splitlines()
ldaten = len(daten)

#test = daten[2]
#test1 = test[test.find(" ")+1:]
#print(test1[:1])
testdaten = input("hier: ")

nummer = 0

poszug = 2
zug = 3
buchstabe = ""
string = "hi"
while poszug < 10:

    for x in daten:

        if testdaten in x:
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

    nächsterzug = string[zug:zug + 1]
    zug += 4
    print("String: ", string)
    print("Arraynr: ", posarray)
    print("Buchstabe: ", buchstabe)
    print("Der Computer macht diesen spielzug: ", nächsterzug)
    nummer += 1
    poszug += 2

print("END String: ", string)
print("Arraynr: ", posarray)
print("Buchstabe: ", buchstabe)
