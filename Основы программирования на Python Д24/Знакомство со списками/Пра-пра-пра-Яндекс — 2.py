a = [input() for _ in range(int(input()))]
w = [input() for _ in range(int(input()))]
print(*list(filter(lambda x: all(i in x for i in w), a)), sep='\n')