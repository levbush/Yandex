li = list(map(lambda x: int(x) ** 2, input().split()))
a, b = map(int, input().split())
print(sum(li[a:b + 1]))