num = int(input())
counter = 0
while num != 1:
    if num % 2:
        num -= 1
    else:
        num //= 2
    counter += 1
print(counter)