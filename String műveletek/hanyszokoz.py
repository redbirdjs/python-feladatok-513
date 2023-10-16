inp = input("Mondat: ")
count = 0

for i in inp:
    if i == ' ': count += 1

print(f"A mondatban {count} szóköz van")
print(f"{str.join('', inp.split(' '))}")