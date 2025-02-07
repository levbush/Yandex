def prime(number: int) -> str:
    for i in range(2, int(number**0.5 + 1)):
        if not (number % i) or number == 1:
            return 'Составное число'
    return 'Простое число'