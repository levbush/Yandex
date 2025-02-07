def eratosthenes(N):
    li = list(range(2, N + 1))
    for i in range(2, int(N**0.5) + 1):
        if li[i - 2] != 0:
            for j in range(i**2, N + 1):
                if j in li and j != i and j % i == 0:
                    print(j, end=' ')
                    li[li.index(j)] = 0