li = [1, 1, 1]
n = int(input())
for i in range(3, n):
    li.append(sum(li[i - 3:i]))
print(*li[:n], sep=' ')