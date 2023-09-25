import random

count = 0
for i in range(0, 20):
    szam = random.randint(1, 12)
    if (szam % 3 == 0):
        count += 1
        print(szam)

print("Összesen", count, "ilyen szám volt.")
        