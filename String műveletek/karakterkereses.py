inp = input("Kérek egy mondatot: ")
keresett = input("Add meg a keresni kívánt karaktert: ")

index = inp.find(keresett) + 1
print(f"A keresett karakter a(z) {index}. helyen áll.")