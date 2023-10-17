inp = input("kérek egy szöveget: ")
torl = input("kérek egy törlendő karaktert: ")

while len(torl) > 1:
    torl = input("kérek egy törlendő karaktert: ")

print(inp.strip(torl))