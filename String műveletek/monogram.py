kettes = ["cs", "zs", "dz", "dzs", "ty", "ly", "sz"]

vnev = input("Kérem a vezetéknevet: ")
knev = input("Kérem a keresztnevet: ")

mono = ""

if vnev[0:2].lower() in kettes:
    mono += vnev[0:2] + "."
else:
    mono += vnev[0:1] + "."
if knev[0:2].lower() in kettes:
    mono += knev[0:2] + "."
else:
    mono += knev[0:1] + "."

print(mono)