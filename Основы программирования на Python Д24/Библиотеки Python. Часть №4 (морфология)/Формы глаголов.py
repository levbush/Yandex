import pymorphy3
from sys import stdin


morph = pymorphy3.MorphAnalyzer()
text = stdin.readlines()
morphed_text = sum([list(map(lambda x: morph.parse(x.strip('»:;\'".,-/!?'))[0].normal_form, line.split())) 
                    for line in text], start=[])
words = ['видеть', 'увидеть', 'глядеть', 'примечать', 'узреть']
print(sum([morphed_text.count(el) for el in words]))