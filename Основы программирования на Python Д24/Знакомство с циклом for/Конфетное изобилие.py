S = int(input())
xmin = S
for m in range(1, int(S**0.5) + 1):
    k, r = divmod(S, m)
    if r == 0:
        for n in [2 * k, k, 2 * m, m]:
            x, r = divmod(2 * S - n * (n - 1), 2 * n)
            if r == 0 and x > 0:
                xmin = min(xmin, x)
print(xmin)