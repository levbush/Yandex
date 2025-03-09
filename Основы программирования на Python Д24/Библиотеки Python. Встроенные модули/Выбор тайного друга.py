from sys import stdin
from random import randint
data = stdin.readlines()
for name in data.copy():
    flag = False
    if name in data:
        flag = True
        data.remove(name)
    print(f'{name.strip()} - {data.pop(randint(0, len(data) - 1)).strip()}')
    if flag:
        data.append(name)