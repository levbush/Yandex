from sys import stdin
from statistics import mean, StatisticsError
try:
    print(mean(map(int, stdin.readlines())))
except StatisticsError:
    print(-1)