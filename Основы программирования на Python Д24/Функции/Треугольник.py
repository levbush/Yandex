def triangle(a: float, b: float, c: float) -> None:
    print('Это треугольник' if sum([a, b, c]) - max([a, b, c]) > max([a, b, c]) else 'Это не треугольник')