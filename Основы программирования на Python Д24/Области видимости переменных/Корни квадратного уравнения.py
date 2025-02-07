def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def roots(a, b, c):
    D = discriminant(a, b, c)
    return [(-b + D ** 0.5) / (2 * a), (-b - D ** 0.5) / (2 * a)]


def larger_root(p, q):
    return max(roots(1, p, q))


def smaller_root(p, q):
    return min(roots(1, p, q))


def main():
    p, q = float(input()), float(input())
    print(discriminant(1, p, q))
    print(smaller_root(p, q), larger_root(p, q))