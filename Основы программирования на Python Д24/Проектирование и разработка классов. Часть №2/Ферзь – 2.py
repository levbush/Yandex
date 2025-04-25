def check_pos(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class ChessPiece:
    def __init__(self, color):
        self.color = color

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return 'w' if self.color == WHITE else 'b'

    def char(self):
        return self.__class__.__name__[0] if self.__class__.__name__ != 'Knight' else 'N'


class Queen(ChessPiece):
    def can_move(self, board, row1, col1, row, col):
        self.row = row1
        self.col = col1
        if ((abs(self.row - row) == abs(self.col - col) or row == self.row or col == self.col) and check_pos(row, col)):
            if board[row][col] and board[row][col].color == self.color:
                return False
            if self.row == row:
                for i in range(min(self.col, col) + 1, max(self.col, col)):
                    if board[self.row][i]:
                        return False
            elif self.col == col:
                for i in range(min(self.row, row) + 1, max(self.row, row)):
                    if board[i][self.col]:
                        return False
            else:
                for i in range(1, max(self.row, row) - min(self.row, row)):
                    if board[self.row + i * (row - self.row) // abs(row - self.row)][
                            self.col + i * (col - self.col) // abs(col - self.col)]:
                        return False
            return True
        return False


class Rook(ChessPiece):
    pass


class Bishop(ChessPiece):
    pass


class Knight(ChessPiece):
    pass


class Pawn(ChessPiece):
    pass


class King(ChessPiece):
    pass


class Board:
    field = []

    def is_under_attack(self, row, col, color):
        for line in self.field:
            for el in line:
                if issubclass(el.__class__, ChessPiece) and el.color == color:
                    if el.can_move(row, col):
                        return True
        return False    
    
    def cell(self, row, col):
        piece = self.field[row][col]
        if piece:
            return f'{piece.get_color()}{piece.char()}'
        else:
            return '  '

    def get_piece(self, row, col):
        return self.field[row][col]
    
    def __getitem__(self, key):
        return self.field[key]
    
    def move_piece(self, row, col, row1, col1):
        if not check_pos(row, col) or not check_pos(row1, col1):
            return False
        piece = self.field[row][col]
        # if piece:
        #     if piece.color == WHITE:
        #         if self.is_under_attack(row1, col1, BLACK):
        #             return False
        #     else:
        #         if self.is_under_attack(row1, col1, WHITE):
        #             return False
        #     if piece.can_move(self, row, col, row1, col1):
        self.field[row1][col1] = piece
        self.field[row][col] = None
        piece.set_position(row1, col1)
        return True
        # return False


WHITE = 1
BLACK = 2