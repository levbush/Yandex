tunnels = dict()
for i in range(int(input())):
    tunnels[i + 1] = list()
    for j in range(int(input())):
        tunnels[i + 1].append(int(input()))
mins = [{i: min(tunnels[i])} for i in tunnels]
minns = list([list(map(int, str(i.items())[13:-3].split(', '))) for i in mins])
maxn = max(minns, key=lambda x: x[1])
maxni = minns.index(maxn)
print(maxni + 1, maxn[1])