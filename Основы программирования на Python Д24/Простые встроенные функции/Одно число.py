n = float(input())
print(1 / n if abs(n) > 1 / 1000000 else 1000000)