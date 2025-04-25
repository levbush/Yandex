import pymorphy3


morph = pymorphy3.MorphAnalyzer()
word = morph.parse(input())[0]
word_singular = word.inflect({'sing'})
word_plural = word.inflect({'plur'})
print(f'''Единственное число:
Именительный падеж: {word_singular.inflect({'nomn'}).word}
Родительный падеж: {word_singular.inflect({'gent'}).word}
Дательный падеж: {word_singular.inflect({'datv'}).word}
Винительный падеж: {word_singular.inflect({'accs'}).word}
Творительный падеж: {word_singular.inflect({'ablt'}).word}
Предложный падеж: {word_singular.inflect({'loct'}).word}
Множественное число:
Именительный падеж: {word_plural.inflect({'nomn'}).word}
Родительный падеж: {word_plural.inflect({'gent'}).word}
Дательный падеж: {word_plural.inflect({'datv'}).word}
Винительный падеж: {word_plural.inflect({'accs'}).word}
Творительный падеж: {word_plural.inflect({'ablt'}).word}
Предложный падеж: {word_plural.inflect({'loct'}).word}''' if 'NOUN' in word.tag else 'Не существительное')