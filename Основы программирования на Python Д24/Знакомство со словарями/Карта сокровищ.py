li = [(lambda inp: int(str(int(inp[0]) // 10) + str(int(inp[1]) // 10)))(input().split()) for _ in range(int(input()))]
ans = 0
for el in set(li):
    x = li.count(el)
    if x > ans:
        ans = x
print(ans)