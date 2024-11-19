n = int(input())
total = 0
for i in range(1, n + 1):
    ni = i
    power = 0
    for j in range(i, 0, -2):
        power += j
    ni **= power
    total += ni
print(total)