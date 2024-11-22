whitelist = [input() for _ in range(int(input()))]
checklist = [input() for _ in range(int(input()))]
for query in checklist:
    if query in whitelist:
        print(query)