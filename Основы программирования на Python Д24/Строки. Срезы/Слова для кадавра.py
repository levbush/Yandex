mask = input()
vowels = 'ауоыиэяюёе'
nonwovels = 'бвгджзйклмнпрстфхцчшщьъ'
li = []
ans = []
while (inp := input()):
    li.append(inp)
if '*' in mask:
    mask = mask.split('*')
    for i in li:
        first = second = True
        if len(i) < len(mask[0]) + len(mask[1]):
            continue
        for j in range(len(mask[0])):
            if mask[0][j] == '0':
                if i[j] not in vowels:
                    first = False
                    break
            elif mask[0][j] == '1':
                if i[j] not in nonwovels:
                    first = False
                    break
        if first:
            for j in range(-1, -len(mask[1]) - 1, -1):
                if mask[1][j] == '0':
                    if i[j] not in vowels:
                        second = False
                        break
                elif mask[1][j] == '1':
                    if i[j] not in nonwovels:
                        second = False
                        break
        if first and second:
            ans.append(i)
else:
    for i in li:
        flag = True
        if len(i) == len(mask):
            for j in range(len(mask)):
                if mask[j] == '0':
                    if i[j] not in vowels:
                        flag = False
                        break
                elif mask[j] == '1':
                    if i[j] not in nonwovels:
                        flag = False
                        break
        else:
            continue
        if flag:
            ans.append(i)
if ans:
    print(*ans, sep='\n')
else:
    print('Есть нечего, значить!')