a = int(input("a oldal: "))
b = int(input("b oldal: "))
c = int(input("magasság: "))

V = a * b * c
A = 2 * (a*b + b*c + c*a)

print(f"Térfogat: {V}")
print(f"Felszín: {A}")