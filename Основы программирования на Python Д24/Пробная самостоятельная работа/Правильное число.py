li = [len(input()) for _ in range(3)]
step = -li.pop(li.index(min(li)))
start, end = max(li), min(li)
print(' '.join(list(str(i) for i in range(start, end, step))))