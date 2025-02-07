data = {}
for _ in range(int(input())):
    s = input()
    data[s.split()[0]] = ' '.join(s.split()[1:])
for _ in range(int(input())):
    print(data.get(input(), 'Нет в словаре'))