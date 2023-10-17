inp = input("Kérek egy mondatot: ")

def fv(input):
    for i in input:
        if (inp.count(i) >= 2):
            return inp.index(i)
    return -1

print(fv(inp))