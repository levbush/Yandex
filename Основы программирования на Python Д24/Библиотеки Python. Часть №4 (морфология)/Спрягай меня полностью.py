import pymorphy3


morph = pymorphy3.MorphAnalyzer()
word = morph.parse(input())[0]
word_past = word.inflect({'past'})
word_present = word.inflect({'pres'})
print(f'''Прошедшее время:
{word_past.inflect({'masc'}).word}
{word_past.inflect({'femn'}).word}
{word_past.inflect({'neut'}).word}
{word_past.inflect({'plur'}).word}
Настоящее время:
{word_past.inflect({'1per', 'sing'}).word}
{word_past.inflect({'1per', 'plur'}).word}
{word_past.inflect({'2per', 'sing'}).word}
{word_past.inflect({'2per', 'plur'}).word}
{word_past.inflect({'3per', 'sing'}).word}
{word_past.inflect({'3per', 'plur'}).word}
''' if 'VERB' in word.tag or 'INFN' in word.tag else 'Не глагол')
