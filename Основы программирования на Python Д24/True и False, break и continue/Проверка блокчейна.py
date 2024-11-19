n = int(input())
blocks = [int(input()) for _ in range(n)]
hl = 0


def f():
    global n, hl, blocks
    for i in range(n):
        b = blocks[i]
        h = b % 256
        r = (b // 256) % 256
        m = (b // 256**2) % 256
        if h != (37 * (m + r + hl)) % 256 or h > 99:
            return i
        hl = h
    return -1


print(f())