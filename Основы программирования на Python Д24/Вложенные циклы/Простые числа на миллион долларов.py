n = int(input())
flag = True
for i in range(2, n):
    for j in range(2, i):
        if i % j == 0:
            flag = False
    if flag:
        print(i)
    flag = True