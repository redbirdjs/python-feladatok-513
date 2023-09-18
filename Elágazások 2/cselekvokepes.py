kor = int(input("Adj meg egy életkort: "))

if (kor < 14):
    print("Cselekvőképtelen")
elif (kor >= 14 and kor < 18):
    print("Korlátozottan cselekvőképes")
else:
    print("Nagykorú")