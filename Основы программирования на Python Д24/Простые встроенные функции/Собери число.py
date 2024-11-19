n = int(input())
n1, n2 = n // 100 + n // 10 % 10, n // 10 % 10 + n % 10
if n1 >= n2:
    print(str(n1) + str(n2))
else:
    print(str(n2) + str(n1))