from sys import stdin


text = ''.join([el for el in stdin.read() if el.isalpha() or el == ' ' or el == '\n']).split()
words = sorted(filter(lambda x: x[1][0].isupper(), enumerate(text)), key=lambda x: x[1])
was = set()
print(*[f'{el[0]} - {el[1]}' for el in words if el[1] not in was and not was.add(el[1])], sep='\n')