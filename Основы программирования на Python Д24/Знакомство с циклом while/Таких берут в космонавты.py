s = input()
counter = 0
hmax, hmin = 150, 190
while s != '!':
    s = int(s)
    if s >= 150 and s <= 190:
        counter += 1
        if hmax < s:
            hmax = s
        if hmin > s:
            hmin = s
    s = input()
print(counter)
print(hmin, hmax)