numbers = [2, 5, 7, 7, 8, 4, 1, 6]
# odd = even = [] Один и тот же список
odd, even = [], []  # Разные списки
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)