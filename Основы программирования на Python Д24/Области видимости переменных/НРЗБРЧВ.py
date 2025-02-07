def translate(text: str):
    mask = 'аеэуюяыоиё' + 'аеэуюяыоиё'.upper() + '.,-'
    for i in mask:
        text = text.replace(i, '')
    text = ' '.join(text.split())
    global translated_text
    translated_text = text.strip()


translated_text = ''
