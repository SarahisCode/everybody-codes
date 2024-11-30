str = input()
pots = 0
for char in str:
    if char == "B":
        pots += 1
    elif char == "C":
        pots += 3
print(pots)
