def check_pos(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True


class ChessPiece:
    def __init__(self, row, col, color):
        self.row, self.col, self.color = row, col, color

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return self.__class__.__name__[0]


class Queen(ChessPiece):
    def can_move(self, row, col):
        if (abs(self.row - row) == abs(self.col - col) or row == self.row or col == self.col) and check_pos(row, col):
            return True
        return False


class Rook(ChessPiece):
    def can_move(self, row, col):
        if (row == self.row or col == self.col) and check_pos(row, col):
            return True
        return False


class Bishop(ChessPiece):
    def can_move(self, row, col):
        if abs(self.row - row) == abs(self.col - col) and check_pos(row, col):
            return True
        return False


class Knight(ChessPiece):
    def can_move(self, row, col):
        if not check_pos(row, col):
            return False
        possible_moves = []
        for x in [1, 2, -1, -2]:
            if x % 2 == 0:
                for y in [1, -1]:
                    if check_pos(self.row + x, self.col + y):
                        possible_moves.append((self.row + x, self.col + y))
            else:
                for y in [2, -2]:
                    if check_pos(self.row + x, self.col + y):
                        possible_moves.append((self.row + x, self.col + y))
        if (row, col) not in possible_moves:
            return False
        return True


class Board:
    field = []

    def is_under_attack(self, row, col, color):
        for line in self.field:
            for el in line:
                if issubclass(el.__class__, ChessPiece) and el.color == color:
                    if el.can_move(row, col):
                        return True
        return False


WHITE = 0
BLACK = 1