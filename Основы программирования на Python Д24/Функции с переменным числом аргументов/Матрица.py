def matrix(n=1, m=None, a=0):
    if m is None:
        m = n
    return [[a] * m for _ in range(n)]