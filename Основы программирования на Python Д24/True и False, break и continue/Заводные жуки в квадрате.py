a = float(input())
speed = float(input())
turns = 0
if a >= speed:
    while abs(a - speed) > 0.01:
        a = (speed**2 + (a - speed)**2)**0.5
        turns += 1
    print(turns)
else:
    print(0)