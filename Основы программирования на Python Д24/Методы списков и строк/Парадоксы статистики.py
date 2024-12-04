from statistics import median, mode
from functools import reduce
medians, modes = [], []
all_li = [list(map(int, input().split())) for _ in range(int(input()))]
for li in all_li:
    medians.append(median(li))
    modes.append(mode(li))
print(*medians)
print(*modes)
print(median(medians))
print(mode(modes))
all_li = reduce(list.__add__, [el for el in all_li])
print(median(all_li))
print(mode(all_li))