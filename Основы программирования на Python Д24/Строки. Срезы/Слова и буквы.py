def f():
    li = []
    while (inp := input()) != 'стоп':
        li.append(inp)
    li = sorted(li, key=len)
    mi, ma = li[0], li[-1]
    for i in mi:
        if i not in ma:
            print('НЕТ')
            return
    print('ДА')


f()