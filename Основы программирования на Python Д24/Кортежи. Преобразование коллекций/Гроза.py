li = [(int(input()), float(input())) for _ in range(int(input()))]
for i in range(len(li)):
    for j in range(len(li)):
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
print(*li, sep='\n')