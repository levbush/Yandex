data = {input() for _ in range(int(input()))}
for _ in range(int(input())):
    s = input().split('/')
    flag = False
    for i in range(len(s) + 1):
        if '/'.join(s[:i]) in data:
            print('YES')
            flag = True
            break
    if not flag:
        print('NO')