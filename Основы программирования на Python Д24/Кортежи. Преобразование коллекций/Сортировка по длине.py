li = [input() for _ in range(int(input()))]
for i in range(len(li)):
    for j in range(len(li)):
        if len(li[i]) < len(li[j]):
            li[i], li[j] = li[j], li[i]
        elif len(li[i]) == len(li[j]):
            if li[i] < li[j]:
                li[i], li[j] = li[j], li[i]
print(*li, sep='\n')