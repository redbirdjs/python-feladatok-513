fizetes = int(input("Mennyit keres havonta József? "))
ev = 2009
nov = 0.12

while (ev < 2026):
    fizetes += fizetes * nov
    ev += 1;

print(f"József fizetése 2026-ban havi {round(fizetes)} lesz.")