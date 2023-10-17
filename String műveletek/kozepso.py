inp = input("Kérek egy szót: ")

if len(inp) % 2 == 0:
    print(f"{inp[int(len(inp)/2)-1:3]}")
else:
    print(f"{inp[int(len(inp)/2)]}")