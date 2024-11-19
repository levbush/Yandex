n = input()
while int(n) < 1000000000 and n[0] != '1':
    n = str(int(n) * int(n[0]))
print(n)