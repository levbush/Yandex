flag = False
for i in range(int(input())):
    n = input().lower()
    if 'кот' in n:
        flag = True
    if 'пёс' in n:
        flag = False
if not flag:
    print('НЕТ')
else:
    print('МЯУ')    