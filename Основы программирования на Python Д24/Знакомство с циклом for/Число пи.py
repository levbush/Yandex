total = 0
for i in range(int(input())):
    total += ((-1) ** i) / (2 * i + 1)
print(total * 4)