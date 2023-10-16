inp = input("Szöveg: ")
count = 0

for i in inp:
    if (i == "i"): count += 1

print(f"A szövegben {count} db I betű található")