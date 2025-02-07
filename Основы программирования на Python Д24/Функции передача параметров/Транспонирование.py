def transpose(matrix):
    ans = list(zip(*matrix))
    matrix.clear()
    for i in range(len(ans)):
        matrix.insert(i, ans[i])