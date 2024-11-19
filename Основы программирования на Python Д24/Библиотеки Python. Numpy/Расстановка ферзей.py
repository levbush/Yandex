import numpy as np


def valid(s, row, col, size):
    for i in range(row):
        if s[i][col] == 1:
            return False
        if col - (row - i) >= 0 and s[i][col - (row - i)] == 1:
            return False
        if col + (row - i) < size and s[i][col + (row - i)] == 1:
            return False
    return True


def solve(s, row, size, solutions):
    if row == size:
        solutions.append(''.join(str(np.where(s[i] == 1)[0][0] + 1) for i in range(size)))
        return
    for col in range(size):
        if valid(s, row, col, size):
            s[row][col] = 1 
            solve(s, row + 1, size, solutions)
            s[row][col] = 0


def queens(size):
    s = np.zeros((size, size), dtype=np.int8)
    solutions = []
    solve(s, 0, size, solutions)
    for solution in sorted(solutions):
        print(solution)