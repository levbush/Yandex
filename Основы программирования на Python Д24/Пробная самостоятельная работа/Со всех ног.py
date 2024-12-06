n = int(input())
key = input()
counter1 = counter2 = 0
for _ in range(n):
    inp = input()
    counter1 += 1
    counter2 += 1 if key in inp or 'забыл' in inp else 0
print('НЕ ТАК И МНОГО' if counter2 <= n // 2 else 'ВСЕ РАВНО НИЧЕГО СТРАШНОГО')
print(counter1 + counter2)