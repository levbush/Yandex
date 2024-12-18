n = int(input())
s = {int(input()) for _ in range(n)}
ans = set()
for i in s:
    for j in s:
        ans.add(i - j)
print(*sorted(ans), sep='\n')