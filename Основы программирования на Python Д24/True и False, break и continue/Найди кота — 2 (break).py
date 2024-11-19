flag = False
n = input()
i = 1
while n != 'СТОП':
    if 'кот' in n.lower():
        flag = True
        break
    n = input()
    i += 1
print(i if flag else (flag - 1))