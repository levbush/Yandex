def swap(a, b):
    if a == b:
        return
    ans = a[:], b[:]
    a.clear()
    b.clear()
    a += ans[1]
    b += ans[0]