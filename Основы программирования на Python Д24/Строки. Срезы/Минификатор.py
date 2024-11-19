li = [input() for _ in range(int(input()))]
for e in range(len(li)):
    el = li[e]
    if '#' in el:
        in_str = False
        elsplit = el.split('#')[0]
        for i in range(len(elsplit)):
            if elsplit[i] == "'":
                if elsplit[i - 1] != '\\':
                    in_str = not in_str
                else:
                    if elsplit[i - 2] == '\\':
                        in_str = not in_str
        if not in_str:
            el = elsplit
    if '  ' in el.lstrip():
        spaces = 0
        for i in el:
            if i == ' ':
                spaces += 1
            else:
                break
        in_str = False
        el = list(el.lstrip())
        i = 0
        while i < len(el):
            try:
                if el[i - 1] == "'":
                    if i > 1 and el[i - 2] != '\\':
                        in_str = not in_str
                    else:
                        if i > 2 and el[i - 3] == '\\':
                            in_str = not in_str
                if not in_str:
                    if el[i - 1] == ' ' and el[i] == ' ':
                        del el[i]
                        i -= 1
                    elif i > 0 and el[i - 2] == ' ' and el[i - 1] == ' ':
                        del el[i - 2]
                        i -= 1
                    elif el[i - 1] == ' ' and el[i] == ' ':
                        del el[i]
                        i -= 1
                i += 1
            except IndexError:
                continue
        el = ' ' * spaces + ''.join(el)
    li[e] = ''.join(el) if isinstance(el, list) else el
print(*li, sep='\n')