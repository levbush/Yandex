def circle_length(radius: float) -> float:
    return 2 * pi * radius


def circle_area(radius: float) -> float:
    return pi * radius**2


def main():
    radius = float(input())
    print(circle_length(radius), circle_area(radius))


pi = 3.14159