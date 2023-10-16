inp = input("Kérek egy szöveget: ")
count = 0

for c in inp:
    if c.islower(): count += 1

print(f"A megadott szövegben {count} kisbetű van")