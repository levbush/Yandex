from random import choice


digits = '1234567890'
num = choice([n for n in range(1000, 10000) if len(set(str(n))) == 4])
# history: (bulls: {position: digit}, cows: {position: list[digit]}, absent: {digit})
history: tuple[dict[int, int], dict[int, list[int]], set[int]] = ({}, {}, set())
was = set()


def parse_num(n):
    return list(map(int, str(n))) if n else n


def check_match(guess):
    number, guess_digits = parse_num(num), parse_num(guess)
    bulls = cows = 0
    for i in range(4):
        if number[i] == guess_digits[i]:
            bulls += 1
        elif guess_digits[i] in number:
            cows += 1
    return bulls, cows


def write(guess, mode=(1, 2)):
    number, guess_digits = parse_num(num), parse_num(guess)
    for i in range(4):
        if number[i] == guess_digits[i]:
            if 1 in mode:
                history[0][i] = guess_digits[i]
        elif guess_digits[i] in number:
            if 1 in mode:
                history[1][i] = guess_digits[i]
        else:
            if 2 in mode:
                history[2].add(guess_digits[i])


def is_historically_correct(guess):
    candidate = int(guess) if isinstance(guess, str) else guess
    digits_list = parse_num(candidate)
    if len(set(digits_list)) != 4 or candidate == num or candidate in was:
        return False
    # Быки: позиции должны точно соответствовать.
    for pos, d in history[0].items():
        if digits_list[pos] != d:
            return False
    # Коровы: цифра должна появиться, но не в том же положении.
    for pos, d in history[1].items():
        if d not in digits_list or digits_list[pos] == d:
            return False
    # Отсутствующие цифры: ни одина из них не должна появиться.
    for d in history[2]:
        if d in digits_list:
            return False
    return True


def receive_guess(guess):
    global num
    bulls, cows = check_match(guess)
    if bulls >= 2 or cows > 2:
        write(guess, (2,))  # Записываем только отсутствующие цифры, т.к. нельзя, чтобы отсутствовало 
        # больше 6 цифр и это нужно учитывать при выборе следующего числа, 
        # но быки и коровы не нужно записывать, так как мы их собираемся менять.
        candidates = [n for n in range(1000, 10000) if is_historically_correct(n)]
        if candidates:
            num = min(candidates, key=lambda x: check_match(x))  # Выбираем минимальный tuple (быки, коровы)
    bulls, cows = check_match(guess)
    write(guess, (1, 2))  # Теперь сохраняем всё.
    was.add(int(guess))
    return bulls, cows


print('Загадано число')
while True:
    q = input('Введите число: ')
    if len(set(q)) != 4 or not q.isdigit():
        print('Некорректное число')
        continue
    bulls, cows = receive_guess(q)
    print(f'Быки: {bulls}, коровы: {cows}')
    if bulls == 4:
        break
print('Вы угадали!')
