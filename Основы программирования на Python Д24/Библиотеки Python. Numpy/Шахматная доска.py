from numpy import ones, int8


def make_field(size):
    s = ones((size, size), dtype=int8)
    for n in range(size):
        if n % 2 == 0:
            for e in range(1, size, 2):
                if e % 2 != 0:
                    s[n][e] = 0
        else:
            for e in range(0, size, 2):
                if e % 2 == 0:
                    s[n][e] = 0
    return s

