li = [input() for i in range(int(input()))]
n = int(input())
flag = False
for i in range(len(li)):
    for j in range(len(li)):
        if int(li[i]) * int(li[j]) == n and i != j:
            flag = True
            break
if flag:
    print('ДА')
else:
    print('НЕТ')
