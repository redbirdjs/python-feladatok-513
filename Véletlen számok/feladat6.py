import random

szamok = ""

for i in range(0, 5):
    szamok += str(random.randint(1, 90)) + " "

print("A mai ötös lottó nyerőszámai:", szamok)