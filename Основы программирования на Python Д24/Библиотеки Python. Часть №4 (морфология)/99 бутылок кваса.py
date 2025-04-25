import pymorphy3


def helper(i):
    return 'Осталась' if i % 10 == 1 and i != 11 else 'Осталось'


morph = pymorphy3.MorphAnalyzer()
word = morph.parse('бутылка')[0]
word2 = morph.parse('Осталось')[0]
for i in range(99, 0, -1):
    print(f'''В холодильнике {i} {word.make_agree_with_number(i).word} кваса.
Возьмём одну и выпьем.
{helper(i - 1)} {i - 1} {word.make_agree_with_number(i - 1).word} кваса.''')