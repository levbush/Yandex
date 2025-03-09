from random import random
count_in = count_all = 0
for _ in range(1000000):
    x, y = random(), random()
    if x**2 + y**2 <= 1:
        count_in += 1
    count_all += 1
print(4 * count_in / count_all)