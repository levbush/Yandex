li = [0]
reversed_li = [0]
n = int(input())
for i in range(n - 1):
    k = 0
    for j in range(i + 1):
        if li[j] == reversed_li[j]:
            k += 1
    reversed_li.insert(0, k)
    li.append(k)
print(*li, sep='\n')