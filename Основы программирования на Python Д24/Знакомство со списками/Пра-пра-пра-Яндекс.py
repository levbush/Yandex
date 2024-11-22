a = [input() for _ in range(int(input()))]
w = input()
print(*list(filter(lambda x: w in x, a)), sep='\n')