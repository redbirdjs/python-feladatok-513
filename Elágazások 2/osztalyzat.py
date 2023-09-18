pontszam = int(input("Hány pontos lett a dogi? "))

if (pontszam < 50):
    print("egyes")
elif (pontszam < 60):
    print("xdd kettes")
elif (pontszam < 70):
    print("hármas")
elif (pontszam < 85):
    print("négyes")
elif (pontszam > 85):
    print("ötös")