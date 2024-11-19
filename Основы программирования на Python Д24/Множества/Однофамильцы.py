data = [input() for _ in range(int(input()))]
print(sum([data.count(i) for i in set(data) if data.count(i) > 1]))
