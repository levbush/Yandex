from datetime import date
from math import sin, pi
physical, emotional, intellectual = 23, 28, 33
birthday, today = input().split("."), input().split(".")
birthday = date(int(birthday[2]), int(birthday[1]), int(birthday[0]))
today = date(int(today[2]), int(today[1]), int(today[0]))
T = (today - birthday).days
for P in physical, emotional, intellectual:
    print(round(sin((2 * pi * T) / P) * 100, 2))