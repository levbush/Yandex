from sys import stdin
print(not all(list(map(int, stdin.read().split()))))