def roots_of_quadratic_equation(a: float, b: float, c: float) -> list[float]:
    if not any((a, b, c)):
        return ['all']
    if not a and not b:
        return []
    if not a:
        return [-c / b]
    D = b ** 2 - 4 * a * c
    if D < 0:
        return []
    if D == 0:
        return [-b / (2 * a)]
    return [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]