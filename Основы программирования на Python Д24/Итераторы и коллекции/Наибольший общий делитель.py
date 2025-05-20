from functools import reduce
from sys import stdin
from math import gcd

print(reduce(gcd, map(int, stdin.readlines())))