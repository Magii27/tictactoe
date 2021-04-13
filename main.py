import math
import random

line1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

print("Spieler X ist an der Reihe")
print("        " + line1[0] + " | " + line1[1] + " | " + line1[2])
print("        " + line1[3] + " | " + line1[4] + " | " + line1[5])
print("        " + line1[6] + " | " + line1[7] + " | " + line1[8])

eingabe = int(input("\nBitte wähle ein Feld aus: "))
test = eingabe - 1

print(test)

print (random.randrange(0,100))


fwrite = open("Daten", "w")
fwrite.write("test")
fread = open("Daten", "r")
einträge = fread.read()

fwrite.close()
print(einträge)
