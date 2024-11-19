d, m, y = int(input()), int(input()), int(input())
c = y // 100
y = y % 100
if m == 1 or m == 2:
    y -= 1
m += 10
if m > 12:
    m -= 12

print((d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7)