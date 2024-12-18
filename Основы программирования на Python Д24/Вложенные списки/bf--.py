li = [0] * 30000
now = 0
for act in input():
    if act == '+':
        li[now] += 1
        if li[now] > 255:
            li[now] = 0
    elif act == '-':
        li[now] -= 1
        if li[now] < 0:
            li[now] = 255
    elif act == '>':
        now += 1
        if now == 30000:
            now = 0
    elif act == '<':
        now -= 1
        if now == -1:
            now = 30000 - 1
    else:
        print(li[now])