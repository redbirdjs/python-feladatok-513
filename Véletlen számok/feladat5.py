import random

print("Véletlen számokat generálunk egy adott tartományban.\n")

lower = int(input("Adj meg egy egész számot, a tartomány elejét: "))
upper = int(input("Adj meg egy egész számot, a tartomány végét: "))
nums = []

for i in range(0, 3):
    nums.append(random.randint(lower, upper))

print("A három véletlen szám a tartományból:", nums[0], nums[1], nums[2])