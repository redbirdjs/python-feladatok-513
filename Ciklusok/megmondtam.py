szam = int(input("Kérek egy számot 1-10 között: "))

while (szam < 0 or szam > 10):
    szam = int(input("Kérek egy számot !!1-10!! között: "))

for i in range(0, szam):
    print(f"Megmondtam már {(i+1)}-szer, hogy semmit nem mondok el kétszer!")