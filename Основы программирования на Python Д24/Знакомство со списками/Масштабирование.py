from numpy import array


rows, cols = int(input()), int(input())
picture = [list(input()) for _ in range(rows)]
picture = array(picture)
picture = picture[::2, ::2]
ans = []
for i in range(len(picture)):
    ans.append(''.join(picture[i]))
print(*ans, sep='\n')