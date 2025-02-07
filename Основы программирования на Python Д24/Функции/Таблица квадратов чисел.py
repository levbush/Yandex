def squared(a, b, k):
    for i in range(a, b + 1):
        if i % 10 == a % 10 and i != a:
            print()
        if i**2 % k:
            print(str(i ** 2).ljust(4), end=' ')