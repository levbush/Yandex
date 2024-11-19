from math import inf
n = inf
nl = n
buyp, sellp = 0, 0
while n != 0:
    n = int(input())
    if n > nl and buyp == 0:
        buyp = n
    elif n < nl and buyp != 0 and sellp == 0:
        sellp = n
    nl = n
print(buyp, sellp, sellp - buyp)