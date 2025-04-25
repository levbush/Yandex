class TicTacToeBoard:
    def __init__(self):
        self.field = [['-' for _ in range(3)] for _ in range(3)]
        self.turn = 'X'

    def new_game(self):
        self.__init__()

    def get_field(self):
        return self.field

    def check_field(self):
        winners = set()
        for i in range(3):
            line = set(self.field[i])
            if line == {'X'}:
                winners.add('X')
            elif line == {'0'}:
                winners.add('0')
        for i in range(3):
            line = set(row[i] for row in self.field)
            if line == {'X'}:
                winners.add('X')
            elif line == {'0'}:
                winners.add('0')
        diag1 = set(self.field[i][i] for i in range(3))
        if diag1 == {'X'}:
            winners.add('X')
        elif diag1 == {'0'}:
            winners.add('0')
        diag2 = set(self.field[i][2 - i] for i in range(3))
        if diag2 == {'X'}:
            winners.add('X')
        elif diag2 == {'0'}:
            winners.add('0')
        if set(sum(self.field, [])) == set('X0') and not winners:
            return 'D'
        elif not winners:
            return None
        elif winners == {'X', '0'}:
            return 'D'
        elif winners == {'X'}:
            return 'X'
        elif winners == {'0'}:
            return '0'

    def make_move(self, row, col):
        state = self.check_field()
        match state:
            case 'X' | '0' | 'D':
                return 'Игра уже завершена'
            case None:
                if self.field[row - 1][col - 1] == '-':
                    self.field[row - 1][col - 1] = 'X' if self.turn == 'X' else '0'
                    state = self.check_field()
                    if state is None:
                        self.turn = '0' if self.turn == 'X' else 'X'
                        return 'Продолжаем играть'
                    elif state == 'D':
                        return 'Ничья'
                    else:
                        return f'Победил игрок {state}'
                else:
                    return f'Клетка {row}, {col} уже занята'