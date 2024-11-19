N = int(input())
for n in range(N):
    for m in range(N):
        n1, n2, n3 = n**2 - m**2, 2 * m * n, n**2 + m**2  
        if n1 > 0 and n2 > 0 and n3 > 0:
            n1f = set()
            for i in range(1, int(n1**0.5) + 1):
                if n1 % i == 0:
                    n1f.add(i)
                    n1f.add(n1 // i)
            n2f = set()
            for i in range(1, int(n2**0.5) + 1):
                if n2 % i == 0:
                    n2f.add(i)
                    n2f.add(n2 // i)
            n3f = set()
            for i in range(1, int(n3**0.5) + 1):
                if n3 % i == 0:
                    n3f.add(i)
                    n3f.add(n3 // i)
            if len(n1f.intersection(n2f).intersection(n3f)) < 2:
                if max(n1, n2, n3) > N:
                    break
                print(n1, n2, n3)