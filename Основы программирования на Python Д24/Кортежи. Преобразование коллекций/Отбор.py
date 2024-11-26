li = [input() for i in range(int(input()))]
print(*li, sep='\n')
print()
print(*[i for i in li if '4' in i or '5' in i], sep='\n')