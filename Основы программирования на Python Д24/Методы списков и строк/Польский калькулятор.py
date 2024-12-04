li = []
for el in input().split():
    if el.isdigit() or el[1:].isdigit():
        li.append(int(el))
    else:
        b, a = li.pop(), li.pop()
        li.append(eval(f'a {el} b'))
print(*li)