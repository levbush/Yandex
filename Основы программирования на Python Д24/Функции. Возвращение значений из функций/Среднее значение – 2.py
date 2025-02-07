from statistics import mean


def average(values: list) -> float:
    return mean(values) if values else 0