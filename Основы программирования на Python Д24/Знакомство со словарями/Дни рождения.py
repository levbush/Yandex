from collections import defaultdict
months = defaultdict(list)
for _ in range(int(input())):
    s = input().split()
    months[s[-1]].append(s[0])
for _ in range(int(input())):
    print(*sorted(months[input()]))