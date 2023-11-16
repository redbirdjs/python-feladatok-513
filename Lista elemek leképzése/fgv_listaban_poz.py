start = -3
stop = 4

lista = []

while (start <= stop):
    lista.append(2*start-3)
    start += 1

nem_negativ = [x for x in lista if x > 0]

print(lista)
print(nem_negativ)