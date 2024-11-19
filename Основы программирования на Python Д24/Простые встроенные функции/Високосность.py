n = int(input())
print('Високосный' if n % 4 == 0 and n % 100 != 0 else 'Високосный' if n % 400 == 0 else 'Не високосный')