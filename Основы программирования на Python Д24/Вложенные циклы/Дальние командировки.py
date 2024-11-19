n = int(input())
d = 9
i = 1
while i * d < n:
    n -= d * i
    d = 10 * d
    i += 1
print(n // i + (int('9' * (i - 1)) if i - 1 != 0 else 0))