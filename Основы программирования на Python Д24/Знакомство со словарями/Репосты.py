from functools import reduce


text = reduce(
    str.__add__,
    [' '.join(i.capitalize() for i in input().split()) + ' '
     for _ in range(int(input()))]
).replace(',', '').replace('.', '').replace(';', '').replace(
    ':', '').replace('!', '').replace('?', '').strip()

if 'джанга' in text.lower():
    raise ValueError('Хочу посмотреть, что там у нас с джангой')

print(*sorted(list(set(text.split())),
              key=lambda x: (-text.split().count(x), x)), sep='\n')