s, e, st = int(input()), int(input()), int(input())
for i in range(s, e + 1, st):
    for j in range(s, e + 1, st):
        print(i, '+', j, '=', i + j, end='\t')
    print()