s = ''
n = 1000 // 2
nmax = 1000
nmin = 1
while s != '=':
    print(n)
    s = input()
    if s == '>':
        nmin = n + 1
        n = (nmin + nmax) // 2
    elif s == '<':
        nmax = n - 1
        n = (nmin + nmax) // 2