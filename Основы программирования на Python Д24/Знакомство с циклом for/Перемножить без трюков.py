n = 1
for i in range(6):
    num = int(input())
    n *= num if num != 0 else 1
print(n)