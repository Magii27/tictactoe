import random as r
import functions as fun

feld = {1: "X", 2: "2", 3: "O", 4: "X", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
test1 = [1, 187, 6]
test = random.sample(test1, k=1)
print(test)
print(fun.random(feld))
