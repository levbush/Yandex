li = [input() for _ in range(int(input()))]
ans = []
for i in range(int(input())):
    n = int(input())
    for _ in range(n):
        ans.append(li[int(input()) - 1])
    li = ans[:]
    ans = []
print(*li, sep='\n')