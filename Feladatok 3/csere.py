import datetime
nev = "Mátrai Gergő"
datum = datetime.datetime.now().strftime("%Y-%m-%d")

print (f"{nev}  | {datum}")

a = 35
b = 27

print(a, b)
[a,b] = [b,a]
print(a, b)