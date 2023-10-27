import datetime

ora = int(input("Óra: "))
perc = int(input("Perc: "))
tperc = int(input("Tart (perc): "))

if (tperc + perc > 60):
    perc = perc + tperc - 60
    ora += 1

print(f"{ora}:{perc}");