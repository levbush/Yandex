n = int(input())
table = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n - 1):
    s = list(map(int, input().split()))
    for el in range(len(s)):
        table[i + 1][el] = s[el]
        table[el][i + 1] = s[el]
a, b = map(int, input().split())
cost = float('inf')
ans = 0
for el in range(len(table[a])):
    temp_cost = 0
    if table[el][b] or el == b:
        temp_cost += table[a][el]
        temp_cost += table[el][b]
    if temp_cost < cost and temp_cost:
        cost = temp_cost
        ans = el
    elif el == b and temp_cost == cost:
        ans = b
print(ans if ans != b else a)
