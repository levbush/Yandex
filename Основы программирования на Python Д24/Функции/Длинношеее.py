def print_long_words(text: str) -> None:
    ru = {'а', 'о', 'э', 'и', 'у', 'ы', 'е', 'ё', 'ю', 'я'}
    en = {'a', 'e', 'i', 'o', 'u', 'y'}
    from re import findall
    words = [word for word in findall(r'[a-zа-яё]+', text.lower())]
    for word in words:
        syllables = sum(1 for el in word if el in ru | en)
        if syllables >= 4:
            print(word)