n = int(input())
counter = 0
while n != 1:
    if not n % 2:
        n /= 2
        counter += 1
    else:
        n *= 3
        n += 1
        counter += 1
print(counter)