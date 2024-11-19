n = float(input())
ans = 0
while n > 0:
    if n > 1000:
        n *= 0.95
    ans += n
    n = float(input())
print(ans)