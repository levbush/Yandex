s = {input() for _ in range(int(input()))}
days = [[input() for _ in range(int(input()))] for _ in range(int(input()))]
for day in days:
    for dish in day:
        if dish in s:
            s.discard(dish)
print(*s, sep='\n')