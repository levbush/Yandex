from collections import defaultdict
months = defaultdict(list)
for _ in range(int(input())):
    s = input().split()
    months[s[-1]].append(' '.join(s[:-1]))
for _ in range(int(input())):
    print(*sorted(months[input()], key=lambda x: (int(x.split()[-1]), x.split()[0])))