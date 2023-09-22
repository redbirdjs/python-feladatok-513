import random

gen = random.randint(100, 200);
tipp = int(input("Találd ki melyik számra gondoltam: "))

if (gen != tipp):
    print("Nem találtad el!")
else:
    print("Eltaláltad, nagyon nagy szerencséd van!")