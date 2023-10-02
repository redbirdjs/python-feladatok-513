penz = 10000
kamat = 0.02
napok = 0

while (penz < 100000):
    penz += penz * kamat
    napok += 1

print(f"10000 Ft-ból {napok} nap múlva lesz 100000 Ft 2%-os kamattal.")