import random

vnev = input("Vezetéknév: ")
knev = input("Keresztnév: ")
szam = random.randint(100, 1000);

vnev = vnev.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ú', 'u').replace('ü', 'u').replace('ű', 'u').replace('ö', 'o').replace('ó', 'o').replace('ő', 'o')
knev = knev.replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ú', 'u').replace('ü', 'u').replace('ű', 'u').replace('ö', 'o').replace('ó', 'o').replace('ő', 'o')

print(f'{vnev[0:3].lower()}{knev[0:3].lower()}{szam}@gmail.com')