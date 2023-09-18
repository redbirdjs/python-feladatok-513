szam = int(input("Kérek egy számot: "))

if szam >= 16:
    szam = szam / 3
    print(szam)
else:
    szam = szam * 10
    print(szam)