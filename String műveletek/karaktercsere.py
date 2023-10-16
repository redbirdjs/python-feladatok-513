inp = input("Kérek egy mondatot: ")
mit = input("Melyik karaktert cseréljem: ")
mire = input("Mire cseréljem: ")

print(f"Eredeti: {inp}")
inp = inp.replace(mit, mire)
print(f"Módosított: {inp}")