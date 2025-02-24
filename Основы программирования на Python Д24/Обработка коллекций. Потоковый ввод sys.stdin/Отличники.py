print('ДА' if all(
    any('5' in el for el in [input() for _ in range(int(input()))]) for _ in range(int(input()))) else 'НЕТ')
