from collections import defaultdict
data = defaultdict(list)
for _ in range(int(input())):
    value, key = input().split()
    data[key].append(value)
for _ in range(int(input())):
    print(*data.get(input(), ['Нет в телефонной книге']))