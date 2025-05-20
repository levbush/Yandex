from sys import stdin


money = []
counter = 0
for line in stdin:
    line = line.strip()
    if line in money:
        counter += int(line.split()[0])
    else:
        money.append(line)
print(counter)