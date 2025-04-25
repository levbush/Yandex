def check_pos(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class ChessPiece:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def char(self):
        return self.__class__.__name__[0] if self.__class__.__name__ != 'Knight' else 'N'


class Queen(ChessPiece):
    pass


class Rook(ChessPiece):
    pass


class Bishop(ChessPiece):
    pass


class Knight(ChessPiece):
    pass


class Pawn(ChessPiece):
    def can_move(self, board, row, col, row1, col1):
        if not check_pos(row1, col1):
            return False
        if board[row1][col1] and self.color == board[row1][col1].color:
            return False
        if self.color == WHITE:
            direction = 1
        else:
            direction = -1
        if row + direction == row1:
            if col1 == col and not board[row1][col1]:
                return True
            if (col1 == col + 1 or col1 == col - 1) and board[row1][col1] and board[row1][col1].color != self.color:
                return True
        return False    


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
        return True
        # return False

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        piece = self.field[row][col]
        if piece.char() != 'P':
            return False
        if piece.can_move(self, row, col, row1, col1):
            if piece.char() == 'P' and (row1 == 0 and piece.color == BLACK or row1 == 7 and piece.color == WHITE):
                self.field[row1][col1] = piece
                self.field[row][col] = None
                char_map = {
                    'Q': Queen,
                    'R': Rook,
                    'B': Bishop,
                    'N': Knight
                }
                self.field[row1][col1] = char_map[char](piece.color)
                return True
            return False
        return False


WHITE = 1
BLACK = 2