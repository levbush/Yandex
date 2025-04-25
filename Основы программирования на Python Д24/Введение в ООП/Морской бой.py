def spreading(row, col, board, last=''):
    try:
        if board[row][col] == 'x':
            if row < 9 and last != '-1+0':
                spreading(row + 1, col, board, '+1+0')
            if row and last != '+1+0':
                spreading(row - 1, col, board, '-1+0')
            if col < 9 and last != '+0-1':
                spreading(row, col + 1, board, '+0+1')
            if col and last != '+0+1':
                spreading(row, col - 1, board, '+0-1')
            if row < 9 and col < 9 and last != '-1-1':
                spreading(row + 1, col + 1, board, '+1+1')
            if row and col < 9 and last != '+1-1':
                spreading(row - 1, col + 1, board, '-1+1')
            if col and row < 9 and last != '-1+1':
                spreading(row + 1, col - 1, board, '+1-1')
            if col and row and last != '+1+1':
                spreading(row - 1, col - 1, board, '-1-1')
        else:
            board[row][col] = '*'
            return
    except RecursionError:
        return


class SeaMap:
    def __init__(self):
        self.board = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, res):
        if res == 'miss' and self.board[row][col] != '*':
            self.board[row][col] = '*'
        elif res == 'hit' and self.board[row][col] != '*':
            self.board[row][col] = 'x'
        elif res == 'sink' and self.board[row][col] != '*':
            self.board[row][col] = 'x'
            spreading(row, col, self.board)

    def cell(self, row, col):
        return self.board[row][col]
