n = int(input())
counter = 0
for i in range(1, n + 1):
    if i == n:
        print(i)
        counter += 1        
    elif n % i == 0:
        print(i, end=' ')
        counter += 1

print('ПРОСТОЕ' if counter == 2 else 'НЕТ')