m = int(input()) * 1000
c = int(input())
for i in range(1, c + 1):
    for j in range(c + 1 - i):
        k = c - i - j
        if i * 20000 + j * 10000 + k * 5000 == m:
            print(i, j, k)