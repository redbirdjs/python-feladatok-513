inp = input("Kérek egy mondatot: ")
count = 0

count += inp.count('A ')
count += inp.count(' a ')
print(f"A szövegben {count}x szerepel az a névelő")