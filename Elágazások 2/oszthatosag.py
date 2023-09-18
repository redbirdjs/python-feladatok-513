szam = int(input("Kérek egy számot: "))

for i in [2,3,5,7]:
    if (szam % i == 0):
        print(f"A szám osztható {i}-vel")