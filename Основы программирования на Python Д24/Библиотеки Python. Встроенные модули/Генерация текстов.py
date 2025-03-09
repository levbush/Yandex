from swift import words  # type: ignore
from collections import defaultdict
from random import choice


words = [word for word in words if word.isalpha()]
data = defaultdict(set)
for i in range(1, len(words)):
    data[words[i - 1]].add(words[i])  # Слова, которые могут идти после каждого слова, без знаков препинания


def gen_text(start_word=choice(list(data.keys())), length=50):
    word = start_word
    text = word.capitalize()
    for _ in range(length):
        word = choice(list(data[word]))  # Выбираем только из слов, которые могут идти после текущего исходя из текста
        text += ' ' + word.lower()
    return text + '.'


print(gen_text(length=int(input())))  # Грамматически правильно всё равно не будет, иначе нужно
# смотреть падеж слов назад в тексте и сохранять его, и ещё много всего