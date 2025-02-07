three = 0


def roman():
    global one, two
    
    def to_roman(num):
        ans = ''
        roman_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        for n, symbol in roman_symbols:
            while num >= n:
                ans += symbol * (num // n)
                num %= n
        return ans
    global three
    three = one + two
    print(f'{to_roman(one)} + {to_roman(two)} = {to_roman(three)}')