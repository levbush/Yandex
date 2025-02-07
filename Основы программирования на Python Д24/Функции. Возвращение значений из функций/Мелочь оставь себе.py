def take_large_banknotes(banknotes: list) -> list:
    return list(filter(lambda x: x > 10, banknotes))