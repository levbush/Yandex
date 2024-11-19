n1, n2 = int(input()), int(input())
eng, deu = {input() for _ in range(n1)}, {input() for _ in range(n2)}
print((n1 + n2 - len(eng & deu) * 2) if (n1 + n2 - len(eng & deu) * 2) != 0 else 'NO')
