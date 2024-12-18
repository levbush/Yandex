n, m = int(input()), int(input())
table = [[input() for _ in range(m)] for _ in range(n)]
for el in table:
    print(*el, sep='\t')
print()
for el in zip(*table):
    print(*el, sep='\t')