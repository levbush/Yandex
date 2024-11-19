n = int(input())
for i in range(n, 0, -1):
    print(*[j + str(i) for j in 'ABCDEFGHI'[:n]])
