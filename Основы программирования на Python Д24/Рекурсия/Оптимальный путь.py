ans = {}


def way(graph, now, path, sump):
    global end, ans
    path.append(now)
    if end in path:
        if now == end:
            ans[sump] = tuple(path)
        return
    else:
        for i in graph:
            if i[0] == now:
                sump += i[-1]
                way(graph, i[1], path, sump)
                path.pop(-1)
                sump -= i[-1]
    if end in path:
        if now == end:
            ans[sump] = tuple(path)
        return


graph = []
s = list(map(int, input().split()))
while len(s) > 2:
    graph.append(s)
    s = list(map(int, input().split()))
start, end = list(map(int, s))
way(graph, start, [], 0)
print(*ans[min(ans)], sep=', ')