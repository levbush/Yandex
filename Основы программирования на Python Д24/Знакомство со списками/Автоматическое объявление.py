a = [input() for _ in range(int(input()))]
b = [int(input()) for _ in range(int(input()))]
print(*[a[i - 1] for i in b], sep='\n')