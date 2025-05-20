from sys import stdin


matrix = [list(map(int, el.split())) for el in stdin.readlines()]
print('YES' if len({sum(el) for el in matrix}.union({sum(el) for el in zip(*matrix)})) == 1 else 'NO')