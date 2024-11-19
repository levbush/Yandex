from numpy import zeros, int64


def snake(rows, cols):
    s = zeros((rows, cols), int64)
    n = 1
    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                s[i][j] = n
                n += 1
        else:
            for j in range(cols - 1, -1, -1):
                s[i][j] = n
                n += 1
    return s

