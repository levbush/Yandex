import numpy as np
x, y = 0, 0


def valids(matrix, x, y):
    s = []
    matrix = np.array(matrix)
    if matrix[x][y] == 0:
        for i in [1, 2, 3, 4]:
            if i not in matrix[x] and i not in matrix[:, y]:
                if x < 2:
                    if y < 2:
                        if i not in matrix[0][:2] and i not in matrix[1][:2]:
                            s.append(i)                        
                    else:
                        if i not in matrix[0][2:] and i not in matrix[1][2:]:
                            s.append(i)
                else:
                    if y < 2:
                        if i not in matrix[2][:2] and i not in matrix[3][:2]:
                            s.append(i)
                    else:
                        if i not in matrix[2][2:] and i not in matrix[3][2:]:
                            s.append(i)
    return s


def solve_sudoku(matrix):
    if len(matrix) == 4:
        matrix.append(0)
        matrix.append(0)
    x = matrix[-2]
    y = matrix[-1]
    if matrix[-1] > 3 and matrix[-2] < 3:
        y -= 4
        x += 1
    if y > 3 and x > 3:
        return
    if 0 not in matrix[0] and 0 not in matrix[1] and 0 not in matrix[2] and 0 not in matrix[3]:
        print(*matrix)
        return
    if matrix[x][y] == 0:
        for i in valids(matrix[:-2], x, y):
            matrix[x][y] = i
            if 0 not in matrix[0] and 0 not in matrix[1] and 0 not in matrix[2] and 0 not in matrix[3]:
                print(*[''.join(list(map(str, [*matrix[j]]))) for j in range(4)], sep='\n')
                return
            matrix[-2], matrix[-1] = x, y
            solve_sudoku(matrix)
            matrix[x][y] = 0
        y += 1
    else:
        y += 1
        matrix[-2], matrix[-1] = x, y
        solve_sudoku(matrix)


matrix = [list(map(int, [*input().strip()])) for _ in range(4)]
solve_sudoku(matrix)