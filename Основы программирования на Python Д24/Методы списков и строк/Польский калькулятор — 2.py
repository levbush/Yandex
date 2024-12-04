from math import factorial
li = []
for el in input().split():
    if el.isdigit() or el[1:].isdigit():
        li.append(int(el))
    elif el == '!':
        li.append(factorial(li.pop()))
    elif el == '~':
        li.append(li.pop() * -1)
    elif el == '#':
        li.extend([li.pop()] * 2)
    elif el == '@':
        li.append(li.pop(-3))
    else:
        b, a = li.pop(), li.pop()
        if el == '/':
            el = '//'
        li.append(eval(f'a {el} b'))
print(*li)