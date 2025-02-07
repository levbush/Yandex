def mirror(arr):
    # mirrored_part = arr.reverse() reverse ничего не возвращает
    mirrored_part = arr[::-1]
    # arr = arr + mirrored_part Не можем изменять arr напрямую
    arr.extend(mirrored_part)