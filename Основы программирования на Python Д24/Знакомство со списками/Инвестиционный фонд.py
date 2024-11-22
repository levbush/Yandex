li = [int(input()) for _ in range(int(input()))]
print(*li, '', *[i * 3 for i in li], sep='\n')