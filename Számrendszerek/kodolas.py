f = input("Fájl neve: ")
sf = ''

for c in f:
    if (c == 'Z'): sf += 'A'
    elif (c == 'z'): sf += 'a'
    else: sf += chr(ord(c) + 1)

print(sf);