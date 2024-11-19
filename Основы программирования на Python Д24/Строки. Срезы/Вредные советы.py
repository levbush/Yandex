li = [input() for _ in range(int(input()))]
for el in li:
    if el[:3].lower() == 'не ':
        el = el[3:]
    print(el)