csv = [input().split(',') for _ in range(int(input()))]
for _ in range(int(input())):
    i, j = map(int, input().split(','))
    print(csv[i][j])