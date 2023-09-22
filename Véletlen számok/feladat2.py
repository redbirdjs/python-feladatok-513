import random

fi = ["fej", "írás"]
tipp = input("Fej vagy írás? ")

valasz = fi[random.randint(0, 1)]

if (tipp == valasz):
    print(f"Válasz: {valasz}\n---------------------------\nEltaláltad!")
else:
    print(f"Válasz: {valasz}\n---------------------------\nNem találtad el!")