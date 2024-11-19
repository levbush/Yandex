num = int(input())
while num > 0:
    n = int(input())
    if n > 3 or n < 1 or n > num:
        pass
    else:
        num -= n
    print(num)