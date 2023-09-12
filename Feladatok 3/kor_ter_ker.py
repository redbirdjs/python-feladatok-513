import math

atmero = int(input("Kör átmérője:"))
sugar = atmero / 2
kerulet = 2 * sugar * math.pi
terulet = sugar ** 2 * math.pi

print(f"Kerület: {kerulet}\nTerület: {terulet}")