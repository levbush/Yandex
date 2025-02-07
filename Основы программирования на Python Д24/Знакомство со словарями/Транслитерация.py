data = """А - A
Б - B
В - V
Г - G
Д - D
Е - E
Ё - E
Ж - ZH
З - Z
И - I
Й - I
К - K
Л - L
М - M
Н - N
О - O
П - P
Р - R
С - S
Т - T
У - U
Ф - F
Х - KH
Ц - TC
Ч - CH
Ш - SH
Щ - SHCH
Ы - Y
Э - E
Ю - IU
Я - IA
Ь - 
Ъ - """

data_dict = {}
for i in data.split('\n'):
    key, value = i.split(' - ')
    data_dict[key] = value

for letter in input():
    if letter in data_dict:
        print(data_dict[letter].capitalize(), end='')
    elif letter.upper() in data_dict:
        print(data_dict[letter.upper()].lower(), end='')
    else:
        print(letter, end='')