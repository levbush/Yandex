from functools import reduce
c1, c2 = 0, 0
colours = reduce(list.__add__, [[input() for _ in range(int(input()))] for _ in range(int(input()))])
for colour in set(colours):
    if colours.count(colour) != 1:
        c1 += 1
        c2 += colours.count(colour)
print(c1, c2)