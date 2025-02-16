def score(sector, num=None):
    return eval('scoring[sector]' + ('[num]' if sector != 'Яблочко' and sector != 'Зеленое_кольцо' else ''))