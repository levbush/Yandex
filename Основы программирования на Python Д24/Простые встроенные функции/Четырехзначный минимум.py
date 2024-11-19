n = int(input())
n1, n2, n3, n4 = n // 1000, n // 100 % 10, n // 10 % 10, n % 10

if n1 == 0:
    n1 += 10
if n2 == 0:
    n2 += 10
if n3 == 0:
    n3 += 10
if n4 == 0:
    n4 += 10

print(min(n1, n2, n3, n4), end='')
if n1 == min(n1, n2, n3, n4):
    n1 = max(n1, n2, n3, n4) + 10
elif n2 == min(n1, n2, n3, n4):
    n2 = max(n1, n2, n3, n4) + 10
elif n3 == min(n1, n2, n3, n4):
    n3 = max(n1, n2, n3, n4) + 10
else:
    n4 = max(n1, n2, n3, n4) + 10

if n1 == 10:
    n1 -= 10
if n2 == 10:
    n2 -= 10
if n3 == 10:
    n3 -= 10
if n4 == 10:
    n4 -= 10


print(min(n1, n2, n3, n4), end='')
if n1 == min(n1, n2, n3, n4):
    n1 = max(n1, n2, n3, n4)
elif n2 == min(n1, n2, n3, n4):
    n2 = max(n1, n2, n3, n4)
elif n3 == min(n1, n2, n3, n4):
    n3 = max(n1, n2, n3, n4)
else:
    n4 = max(n1, n2, n3, n4)

print(min(n1, n2, n3, n4), end='')
if n1 == min(n1, n2, n3, n4):
    n1 = max(n1, n2, n3, n4)
elif n2 == min(n1, n2, n3, n4):
    n2 = max(n1, n2, n3, n4)
elif n3 == min(n1, n2, n3, n4):
    n3 = max(n1, n2, n3, n4)
else:
    n4 = max(n1, n2, n3, n4)

print(min(n1, n2, n3, n4), end='')
if n1 == min(n1, n2, n3, n4):
    n1 = max(n1, n2, n3, n4)
elif n2 == min(n1, n2, n3, n4):
    n2 = max(n1, n2, n3, n4)
elif n3 == min(n1, n2, n3, n4):
    n3 = max(n1, n2, n3, n4)
else:
    n4 = max(n1, n2, n3, n4)