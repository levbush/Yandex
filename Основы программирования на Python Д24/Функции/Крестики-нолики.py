def tic_tac_toe(field):
    for row in field:
        if set(row) == set('x'):
            print('x win')
            return
        elif set(row) == set('0'):
            print('0 win')
            return
    for col in list(zip(*field)):
        if set(col) == set('x'):
            print('x win')
            return
        elif set(col) == set('0'):
            print('0 win')
            return
    maind = set(field[i][i] for i in range(len(field)))
    sided = set(field[i][len(field) - i - 1] for i in range(len(field)))
    if maind == set('x'):
        print('x win')
        return
    elif maind == set('0'):
        print('0 win')
        return
    if sided == set('x'):
        print('x win')
        return
    elif sided == set('0'):
        print('0 win')
        return
    print('draw')