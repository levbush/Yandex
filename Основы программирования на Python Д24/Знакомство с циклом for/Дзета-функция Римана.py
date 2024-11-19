from math import pi
total = 0
for i in range(1, int(input()) + 1):
    total += 1 / i ** 2
print(pi**2 / total)