from string import ascii_letters, digits
from random import choices, choice, shuffle

symbols = ''.join(c for c in ascii_letters + digits if c not in 'Il1Oo0')
letters_lower = symbols[:24]
letters_upper = symbols[24:48]
was = set()


def generate_password(m):
    while True:
        ans = [choice(digits[2:]), choice(letters_lower), choice(letters_upper)] + choices(symbols, k=m - 3)
        shuffle(ans)
        ans = ''.join(ans)
        if ans not in was:
            was.add(ans)
            return ''.join(ans)


def main(n, m):
    return [generate_password(m) for _ in range(n)]