k, e = 0, 0
n = 1
ln = n
while n != '':
    n = input()
    if n == 'Какой подарок?':
        if ln == 'добрый' and k > e:
            print('серебряный шиллинг')
            k, e, ln, n = 0, 0, 0, 0
            continue
        elif ln == 'злой' and e > k:
            print('золотой')
            k, e, ln, n = 0, 0, 0, 0
            continue
        else:
            print('Ах, не знаю!')
            break
    elif n == 'добрый':
        k += 1
    else:
        e += 1
    ln = n if n != 'Какой подарок?' else ln