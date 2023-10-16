inp = input("Kérek valami szöveg izét: ")
inp2 = input("Kérek még egy szöveg izét: ")

for i in inp:
    if (inp2.__contains__(i)):
        inp = inp.replace(i, "")
        
print(inp)