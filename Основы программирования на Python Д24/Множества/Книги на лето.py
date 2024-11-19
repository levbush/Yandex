n1, n2 = int(input()), int(input())
lib, q = {input() for _ in range(n1)}, [input() for _ in range(n2)]
for book in q:
    print('YES' if book in lib else 'NO')
