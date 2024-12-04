queue = []
for i in [input() for _ in range(int(input()))]:
    if 'встал в очередь' in i:
        queue.append(i[:-17])
    elif 'встала в очередь' in i:
        queue.append(i[:-18])
    elif 'будет за тобой' in i:
        queue.insert(queue.index(i[8:i.index('!')]) + 1, i[i.index('!') + 2:-16])
    else:
        queue.remove(i[:-34])
print(*queue, sep='\n')