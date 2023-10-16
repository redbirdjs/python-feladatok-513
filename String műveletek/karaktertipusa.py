kar = input("Kérek egy karaktert: ")

while len(kar) > 1:
    kar = input("Kérek egy karaktert: ")

if kar.isalpha():
    if kar.isupper(): print("A karakter nagybetű")
    elif kar.islower(): print("A karakter kisbetű")
elif kar.isdigit():
    print("A karakter szám")
else:
    print("A karakter valami egyéb")