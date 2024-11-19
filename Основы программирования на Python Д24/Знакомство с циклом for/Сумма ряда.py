total = 0
turn = 1
for i in range(int(input())):
    n = int(input()) * turn
    total += n
    turn *= -1
print(total)