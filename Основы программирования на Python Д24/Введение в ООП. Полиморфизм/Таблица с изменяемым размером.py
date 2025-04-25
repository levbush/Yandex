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

    def delete_row(self, row):
        self.table.pop(row)
        self.rows -= 1
        
    def add_row(self, row):
        self.table.insert(row, [0] * self.cols)
        self.rows += 1
        
    def delete_col(self, col):
        for i in range(self.rows):
            self.table[i].pop(col)
        self.cols -= 1

    def add_col(self, col):
        for i in range(self.rows):
            self.table[i].insert(col, 0)
        self.cols += 1