from string import ascii_letters, digits
from random import choices

symbols = ''.join(c for c in ascii_letters + digits if c not in 'Il1Oo0')


def generate_password(m):
    return ''.join(choices(symbols, k=m))


def main(n, m):
    return list({generate_password(m) for _ in range(n * 10)})[:n]