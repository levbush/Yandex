from functools import reduce
from sys import stdin


print(reduce(lambda x, y: [x, y][x > y], stdin.readlines()))