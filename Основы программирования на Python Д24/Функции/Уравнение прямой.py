def equation(a, b):
    a, b = list(map(float, a.split(';'))), list(map(float, b.split(';')))
    if a[0] == b[0]:
        print(a[0])
    elif a[-1] == b[-1]:
        print(a[-1])
    else:
        dx, dy = a[0] - b[0], a[-1] - b[-1]
        k = dy / dx
        b = a[-1] - a[0] * k
        print(k, b)