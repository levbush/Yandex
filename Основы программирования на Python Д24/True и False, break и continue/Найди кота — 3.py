flag = False
n = input()
i = 1
ansi = 0
counter = 0
while n != 'СТОП':
    if 'кот' in n.lower():
        flag = True
        if ansi == 0:
            ansi = i
        counter += 1
        
    n = input()
    i += 1
print(counter, ansi if flag else (flag - 1))