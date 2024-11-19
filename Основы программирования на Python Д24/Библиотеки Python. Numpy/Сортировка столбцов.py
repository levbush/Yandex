import numpy as np
import random


def super_sort(rows, cols):
    a = np.random.randint(1, 101, size=(rows, cols))
    b = a[:]
    b[:, ::2] = np.sort(b[:, ::2], axis=0)
    b[:, 1::2] = np.sort(b[:, 1::2], axis=0)[::-1]
    return (a, b)

