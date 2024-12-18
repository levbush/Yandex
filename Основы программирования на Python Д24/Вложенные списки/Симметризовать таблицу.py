n = int(input())
table = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n - 1):
    s = list(map(int, input().split()))
    for el in range(len(s)):
        table[i + 1][el] = s[el]
        table[el][i + 1] = s[el]

print(*[' '.join(list(map(str, el))) for el in table], sep='\n')