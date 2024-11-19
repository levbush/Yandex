flag = False
for i in range(int(input())):
    if 'кот' in input().lower():
        print('МЯУ')
        flag = True
        break
if not flag:
    print('НЕТ')