from functools import reduce
nl = []
for j in range(1, 10000):
    a = list(set(reduce(list.__add__, ([i, j // i] for i in range(1, int(j**0.5) + 1) if j % i == 0))))
    a.pop(a.index(j))
    nl.append(a)
for i in range(1, len(nl) + 1):
    for j in range(i + 1, len(nl) + 1):
        if sum(nl[i - 1]) == j and sum(nl[j - 1]) == i and i != j:
            print(i, j)