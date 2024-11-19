from math import factorial
while True:
    n = int(input())
    act = input()
    if act == '+':
        print(n + int(input()))
    elif act == '-':
        print(n - int(input()))
    elif act == '*':
        print(n * int(input()))
    elif act == '/':
        n1 = int(input())
        if n1 != 0:
            print(n // n1)
    elif act == '%':
        n1 = int(input())
        if n1 != 0:
            print(n % n1)
    elif act == '!':
        if n >= 0:
            print(factorial(n))
    elif act == 'x':
        print(n)
        break