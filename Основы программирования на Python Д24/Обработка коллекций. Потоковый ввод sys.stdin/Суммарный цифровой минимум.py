from sys import stdin
print(min(map(int, stdin.readlines()), key=lambda x: (sum(list(map(int, list(str(x))))), -len(str(x)), x)))