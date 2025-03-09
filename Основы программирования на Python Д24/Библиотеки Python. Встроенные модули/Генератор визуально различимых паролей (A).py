from string import ascii_letters, digits
from random import sample

symbols = ''.join(c for c in ascii_letters + digits if c not in 'Il1Oo0')


def generate_password(m):
    return ''.join(sample(symbols, m))


def main(n, m):
    return list({generate_password(m) for _ in range(n * 10)})[:n]