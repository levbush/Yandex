n1, n2 = int(input()), int(input())
for i in range(1, n2 + 1):
    for j in range(1, n1 + 1):
        print(j / i, end=' ')
    print()