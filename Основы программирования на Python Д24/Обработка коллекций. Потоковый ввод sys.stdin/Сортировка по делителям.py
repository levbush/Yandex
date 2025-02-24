from functools import reduce

print(sorted(
    [(n, len(set(reduce(list.__add__, [[i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0])))) for n in
     map(int, iter(input, '0'))], key=lambda x: x[::-1]))