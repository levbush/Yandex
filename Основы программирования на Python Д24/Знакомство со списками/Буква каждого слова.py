a = [input() for _ in range(int(input()))]
i = int(input())
print(*[j[i - 1] for j in a if i <= len(j)], sep='')