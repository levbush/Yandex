n, m = int(input()), int(input())
table = [[input() for _ in range(m)] for _ in range(n)]
print(*[table[0][i] for i in range(m)], sep='\t')
for el in table[1:-1]:
    print(*sorted(el), sep='\t')
if n > 1:
    print(*[table[-1][i] for i in range(m)], sep='\t')