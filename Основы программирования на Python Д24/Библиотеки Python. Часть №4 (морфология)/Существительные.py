import pymorphy3
from sys import stdin
from collections import Counter


morph = pymorphy3.MorphAnalyzer()
text = [el.strip('.,/:;«»-—!?') for el in stdin.read().lower().split() if el.strip('.,/:;«»-—!?')]
count = Counter(morph.parse(word)[0].normal_form for word in text 
                if morph.parse(word)[0].tag.POS == 'NOUN' and morph.parse(word)[0].score > 0.5)
print(*sorted(count, key=lambda x: (count[x], x), reverse=True)[:10])