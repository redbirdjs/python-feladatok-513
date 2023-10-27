szam1 = -1
szam2 = -1

while szam1 > 20 or szam1 < 1:
    szam1 = int(input("Add meg az első számot (1-20): "))

while szam2 > 20 or szam2 < 1:
    szam2 = int(input("Add meg a második számot (1-20): "))

x = abs(szam1-szam2)

print('---------------------------')
for _ in range(0, x):
    print("X", end="")