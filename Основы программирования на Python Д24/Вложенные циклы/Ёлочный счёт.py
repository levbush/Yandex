ns = [i for i in range(1, int(input()) + 1)]
c = 1
while True:
    try:
        for i in range(c):
            print(ns[i], end=' ')
        ns = ns[c:]
        c += 1
        print()
    except IndexError:
        break