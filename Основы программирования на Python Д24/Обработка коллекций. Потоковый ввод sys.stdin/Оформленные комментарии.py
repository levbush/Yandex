from sys import stdin


counter = 0
for line in stdin.readlines():
    counter += 1
    if line.strip() and line.strip()[0] == '#':
        print(f'Line {counter}: {line.strip()[1:].strip()}')