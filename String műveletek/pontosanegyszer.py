inp = input("Kérek egy szöveget: ")
karakterek = []

for i in inp:
    if (inp.count(i) == 1):
        karakterek.append(i)

print("A szövegben egyszer fordulnak elő ezek a karakterek: ", str.join(', ', karakterek))