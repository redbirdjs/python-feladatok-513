import random

number = random.randint(1, 4);
tipp = int(input("Kérek egy számot [1-3]: "))

if (number == tipp):
    print("A számod megegyezik a program által választottal")
elif (number > tipp):
    print("A számod kisebb mint a program által generált")
else:
    print("A számod nagyobb mint a program által generált")