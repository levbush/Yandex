def golden_ratio(i):
    n = 1
    nlast = n
    for _ in range(i - 1):
        n, nlast = n + nlast, n
    print(n / nlast)