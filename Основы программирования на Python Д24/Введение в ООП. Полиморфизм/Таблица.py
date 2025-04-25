class Table:
    def __init__(self, row, col):
        self.rows, self.cols = row, col
        self.table = [[0 for _ in range(col)] for _ in range(row)]

    def get_value(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.table[row][col]

    def set_value(self, row, col, value):
        self.table[row][col] = value

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols
