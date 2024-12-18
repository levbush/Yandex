li = [int(input()) for _ in range(int(input()))]
mi, ma = int(input()), int(input())
print(*list(filter(lambda x: mi <= x <= ma, li)), sep='\n')