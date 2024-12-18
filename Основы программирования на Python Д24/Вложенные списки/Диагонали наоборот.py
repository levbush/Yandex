n = int(input())
table = [list(map(int, input().split(', '))) for _ in range(n)]
total = 0
for i in range(n):
    table[i][i], table[i][n - i - 1] = table[i][n - i - 1], table[i][i]
    total += table[i][i] + table[i][n - i - 1]
print(*[' '.join(list(map(str, el))) for el in table], sep='\n')
print(total)