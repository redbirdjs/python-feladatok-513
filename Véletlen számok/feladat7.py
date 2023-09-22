import random

ora1 = random.randint(1, 24)
perc1 = random.randint(1, 60)

ora2 = random.randint(1, 24)
perc2 = random.randint(1, 60)

orakulonbseg = abs(ora2 - ora1)
perckulonbseg = abs(perc2 - perc1)

print("Idő 1: ", ora1, ":", perc1, sep="")
print("Idő 2: ", ora2, ":", perc2, sep="")
print("-----------------------")
print("A két idő különbsége: ", orakulonbseg, ":", perckulonbseg, sep="")