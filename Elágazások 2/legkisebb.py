tomb = []

for i in range(0, 3):
    tomb.append(int(input("Kérek számot: ")))

tomb.sort()
print(f"A legkisebb szám: {tomb[0]}")