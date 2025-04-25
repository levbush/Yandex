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
    def __init__(self, color):
        super().__init__(color)
        self.can_castle = True


class Bishop(ChessPiece):
    pass


class Knight(ChessPiece):
    pass


class Pawn(ChessPiece):
    pass   


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color)
        self.can_castle = True


class Board:
    def __init__(self):
        self.field = []
        self.turn = WHITE

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
            return ('w' if piece.color else 'b') + piece.char()
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
        if isinstance(piece, King) or isinstance(piece, Rook):
            piece.can_castle = False
        return True
        # return False

    def castling0(self):
        row, col = 0 if self.turn == WHITE else 7, 4
        col1 = 2
        king, rook = self.field[row][col], self.field[row][0]
        if not isinstance(rook, Rook) or not isinstance(king, King) or not rook.can_castle or not king.can_castle:
            return False
        if self.field[row][1] or self.field[row][2] or self.field[row][3]:
            return False
        self.field[row][col1] = king
        self.field[row][col] = None
        self.field[row][col1 + 1] = rook
        self.field[row][0] = None
        king.can_castle = False
        rook.can_castle = False
        self.turn = not self.turn
        return True
    
    def castling7(self):
        row, col = 0 if self.turn == WHITE else 7, 4
        col1 = 6
        king, rook = self.field[row][col], self.field[row][7]
        if not isinstance(rook, Rook) or not isinstance(king, King) or not rook.can_castle or not king.can_castle:
            return False
        if self.field[row][5] or self.field[row][6]:
            return False
        self.field[row][col1] = king
        self.field[row][col] = None
        self.field[row][col1 - 1] = rook
        self.field[row][7] = None
        king.can_castle = False
        rook.can_castle = False
        self.turn = not self.turn
        return True


WHITE = True
BLACK = False