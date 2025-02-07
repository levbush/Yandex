def horizontal_mirror(field: list[str]) -> list[str]:
    return [el[::-1] for el in field]  # Разворот каждой строки, строки отражаются


def vertical_mirror(field: list[str]) -> list[str]:
    return field[::-1]  # Верхние стоки становятся нижними и наоборот, столбцы отражаются


def transposition(field: list[str]) -> list[str]:
    return [''.join(el) for el in zip(*field)]  # Разворот поля на 90°, строки и столбцы 
    # меняются местами


field = [input().strip() for _ in range(4)]
print('\n(исходное поле)', *field, sep='\n', end='\n\n')
print('(горизонтальное отражение)', *horizontal_mirror(field), end='\n\n', sep='\n')
print('(вертикальное отражение)', *vertical_mirror(field), end='\n\n', sep='\n')
print('(транспонирование)', *transposition(field), end='\n\n', sep='\n')
print('(отражение вдоль горизонтали и вертикали)', *vertical_mirror(horizontal_mirror(field)), end='\n\n', sep='\n')
print('(транспонирование, затем вертикальное отражение)', *transposition(horizontal_mirror(field)), end='\n\n', sep='\n')
print('(транспонирование, затем горизонтальное отражение)', *transposition(vertical_mirror(field)), end='\n\n', sep='\n')
print('(транспонирование, затем два отражения)', *transposition(vertical_mirror(horizontal_mirror(field))), sep='\n')
