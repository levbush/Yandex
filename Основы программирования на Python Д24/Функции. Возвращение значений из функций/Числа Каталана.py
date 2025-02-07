def catalan(n: int) -> int:
    if n <= 1:
        return 1
    return int((2 * (2 * n - 1) * catalan(n - 1)) // (n + 1))