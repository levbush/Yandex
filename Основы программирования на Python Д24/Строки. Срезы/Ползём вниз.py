way = input()
symbol = way[0]
counter = 1
now = 1
lasti = ''
ans = [[symbol]]
for i in way[1:] + ' ':
    if i != lasti:
        if lasti == '>':
            for _ in range(counter):
                ans[-1].append(symbol)
                now += 1
        elif lasti == '<':
            for j in range(counter):
                ans[-1][-(j + 1) - 1] = symbol
                now -= 1
        elif lasti == 'V':
            for _ in range(counter):
                ans.append([' ' for _ in range(now)])
                ans[-1][now - 1] = symbol
        counter = 1
    else:
        counter += 1
    lasti = i
print(*[''.join(i) for i in ans], sep='\n')