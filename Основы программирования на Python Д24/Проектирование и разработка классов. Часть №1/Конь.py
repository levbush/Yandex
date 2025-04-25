def check_pos(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True


class Knight:
    def __init__(self, row, col, color):
        self.row, self.col, self.color = row, col, color

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

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return 'N'