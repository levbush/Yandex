from math import lcm, gcd
total = 0
decimals = []
ans = [0, 0]
n = int(input())
for _ in range(n):
    decimals.append([int(input()), int(input())])
lcmd = lcm(*[decimals[i][-1] for i in range(n)])

for i in decimals:
    i[0] = i[0] * int(lcmd / i[1])
    i[1] = lcmd

for i in decimals:
    ans[0] += i[0]
ans[1] = i[1]

gcdd = gcd(*ans)

print(int(ans[0] / gcdd), int(ans[1] / gcdd), sep='/')