lista = []

for i in range(10):
    lista.append(input("Kérek egy szót: "))

print(str.join(" ", lista))
lista.reverse()
print(str.join(" ", lista))