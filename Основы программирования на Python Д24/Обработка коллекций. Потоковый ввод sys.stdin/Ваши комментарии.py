from sys import stdin
print(sum(1 if el.strip() and el.strip()[0] == '#' else 0 for el in stdin.readlines()))