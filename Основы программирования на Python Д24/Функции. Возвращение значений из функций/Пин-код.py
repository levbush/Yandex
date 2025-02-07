def check_pin(pin: str) -> str:
    def prime(number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, int(number**0.5 + 1)):
            if number % i == 0:
                return False
        return True
    pin = pin.split('-')
    if len(pin) != 3:
        return 'Некорректен'
    if not prime(int(pin[0])):
        return 'Некорректен'
    if pin[1] != pin[1][::-1]:
        return 'Некорректен'
    from math import log2
    c = int(pin[2])
    if c <= 0 or log2(c) != int(log2(c)):
        return 'Некорректен'
    return 'Корректен'
