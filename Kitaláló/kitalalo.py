import random

file = open("szavak.txt", "r")
szavak = file.readline().replace('"', '').replace(',', '').split(' ')
rejtett = szavak[random.randint(0, len(szavak))];
segitseg = ""
tippek = 1

megfejtes = input("Kérem a tippet: ")
while (megfejtes != rejtett):
    if (megfejtes == 'stop'):
        break
    segitseg = ""
    for i in range(0, len(rejtett)):
        if (rejtett[i] == megfejtes[i]):
            segitseg += megfejtes[i]
        else:
            segitseg += "."
    print(f"Az eredmény: {segitseg}\n")
    tippek += 1;
    megfejtes = input("Kérem a tippet: ")
if (megfejtes != 'stop'):
    print(f"{tippek} tippeléssel sikerült kitalálni.")