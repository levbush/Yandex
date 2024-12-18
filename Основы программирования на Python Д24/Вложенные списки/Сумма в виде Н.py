n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        temp = 0
        try:
            temp += table[i][j]
            temp += table[i + 1][j]
            temp += table[i + 2][j]
            temp += table[i][j + 2]
            temp += table[i + 1][j + 1]
            temp += table[i + 1][j + 2]
            temp += table[i + 2][j + 2]
        except IndexError:
            continue
        if temp > ans:
            ans = temp
print(ans)