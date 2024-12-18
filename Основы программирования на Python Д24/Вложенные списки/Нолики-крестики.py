table = [input() for _ in range(int(input()))]
if any(['ooo' in el for el in table]) or any(['ooo' in ''.join(el) for el in zip(*table)]):
    print('o')
elif any(['xxx' in el for el in table]) or any(['xxx' in ''.join(el) for el in zip(*table)]):
    print('x')
else:
    print('-')