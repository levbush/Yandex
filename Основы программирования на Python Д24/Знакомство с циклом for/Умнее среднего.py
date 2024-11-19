from statistics import mean
total = 0
iqs = []
n1 = int(input())
n = int(input())
average = n
for i in range(n1 - 1):
    if n > average:
        print('>')
    elif n < average:
        print('<')
    else:
        print(0)
    iqs.append(n)
    average = mean(iqs)
    n = int(input())
if n > average:
    print('>')
elif n < average:
    print('<')
else:
    print(0)
