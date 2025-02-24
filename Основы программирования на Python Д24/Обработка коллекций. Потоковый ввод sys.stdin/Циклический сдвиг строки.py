from sys import stdin
n = int(input())
for el in stdin.readlines():
    print(el.strip('\n')[n % (len(el) - 1):] + el.strip('\n')[:n % (len(el) - 1)])