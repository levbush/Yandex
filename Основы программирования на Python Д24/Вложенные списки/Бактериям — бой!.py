n = int(input())
matrix = [[int(input()) for _ in range(n)] for _ in range(n)]
k = int(input())
for _ in range(k):
    j, i = int(input()), int(input())
    matrix[i][j] -= min(4, matrix[i][j])
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if 0 <= i + di < n and 0 <= j + dj < n:
                matrix[i + di][j + dj] -= min(4, matrix[i + di][j + dj])
print(*[' '.join(map(str, row)) for row in matrix], sep='\n')