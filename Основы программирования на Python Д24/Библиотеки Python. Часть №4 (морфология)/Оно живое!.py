import pymorphy3
from sys import stdin


morph = pymorphy3.MorphAnalyzer()
word1 = morph.parse('живой')[0]
for word in stdin.readlines():
    word = morph.parse(word.strip())[0]
    if 'NOUN' not in word.tag:
        print('Не существительное')
        continue
    print((
                  ('не ' if 'anim' not in word.tag else '') 
                  + word1.inflect({word.tag.gender, 
                                   'nomn'} if 'plur' not in word.tag else {'nomn', 
                                                                           'plur'}).word).capitalize())