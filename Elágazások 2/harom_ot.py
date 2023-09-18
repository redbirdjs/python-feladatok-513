szam = int(input("Give number "))

if (szam % 3 == 0 or szam % 5 == 0):
    print("A szám osztható 3-mal vagy öttel")
else:
    print("A szám nem osztható se 3-mal, sem 5-tel")