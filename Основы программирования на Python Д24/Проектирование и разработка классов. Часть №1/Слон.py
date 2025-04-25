def check_pos(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True


class Bishop:
    def __init__(self, row, col, color):
        self.row, self.col, self.color = row, col, color

    def can_move(self, row, col):
        if abs(self.row - row) == abs(self.col - col) and check_pos(row, col):
            return True
        return False

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def get_color(self):
        return self.color

    def char(self):
        return 'B'