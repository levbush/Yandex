def check_pos(row, col):
    if 0 <= row < 8 and 0 <= col < 8:
        return True


class ChessPiece:
    def __init__(self, row, col, is_white):
        self.row, self.col, self.is_white = row, col, is_white

    def set_position(self, row1, col1):
        self.row = row1
        self.col = col1

    def __str__(self):
        return ('w' if self.is_white else 'b') + \
               (self.__class__.__name__[0]
                if self.__class__.__name__ != 'Knight' else 'N')
    
    def copy(self):
        return eval(self.__class__.__name__)(self.row, self.col, self.is_white)


class Queen(ChessPiece):
    def can_move(self, row, col, board, move=False):
        if ((abs(self.row - row) == abs(self.col - col) or row == self.row or col == self.col) and check_pos(row, col)):
            if board[row][col] and board[row][col].is_white == self.is_white:
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
            if move:
                board[row][col] = self
                board[self.row][self.col] = Nothing()
                self.set_position(row, col)
            return True
        return False


class Rook(ChessPiece):
    def __init__(self, row, col, is_white):
        super().__init__(row, col, is_white)
        self.can_castle = True

    def can_move(self, row, col, board, move=False):
        if (row == self.row or col == self.col) and check_pos(row, col):
            if board[row][col] and board[row][col].is_white == self.is_white:
                return False
            if self.row == row:
                for i in range(min(self.col, col) + 1, max(self.col, col)):
                    if board[self.row][i]:
                        return False
            else:
                for i in range(min(self.row, row) + 1, max(self.row, row)):
                    if board[i][self.col]:
                        return False
            if move:
                self.can_castle = False
                board[row][col] = self
                board[self.row][self.col] = Nothing()
                self.set_position(row, col)
            return True
        return False


class Nothing:
    def __bool__(self):
        return False

    def __str__(self):
        return '  '
    
    def __eq__(self, value):
        return False
    
    def copy(self):
        return Nothing()


class Bishop(ChessPiece):
    def can_move(self, row, col, board, move=False):
        if abs(self.row - row) == abs(self.col - col) and check_pos(row, col):
            if board[row][col] and board[row][col].is_white == self.is_white:
                return False
            for i in range(1, max(self.row, row) - min(self.row, row)):
                if board[self.row + i * (row - self.row) // abs(row - self.row)][
                        self.col + i * (col - self.col) // abs(col - self.col)]:
                    return False
            if move:
                board[row][col] = self
                board[self.row][self.col] = Nothing()
                self.set_position(row, col)
            return True
        return False


class Knight(ChessPiece):
    def can_move(self, row, col, board, move=False):
        if not check_pos(row, col):
            return False
        if board[row][col] and board[row][col].is_white == self.is_white:
            return False
        possible_moves = []
        for x in [2, -2]:
            for y in [1, -1]:
                if check_pos(self.row + x, self.col + y):
                    possible_moves.append((self.row + x, self.col + y))
        for x in [1, -1]:
            for y in [2, -2]:
                if check_pos(self.row + x, self.col + y):
                    possible_moves.append((self.row + x, self.col + y))
        if (row, col) not in possible_moves:
            return False
        if move:
            board[row][col] = self
            board[self.row][self.col] = Nothing()
            self.set_position(row, col)
        return True


class Pawn(ChessPiece):
    def __init__(self, row, col, is_white):
        super().__init__(row, col, is_white)
        self.first_move = True
        self.direction = -1 if self.is_white else 1

    def can_move(self, row, col, board, move=False):
        if not check_pos(row, col):
            return False
        if board[row][col] and board[row][col].is_white == self.is_white:
            return False
        
        if self.col == col and not board[row][col]:
            if self.row - row == self.direction:
                if move:
                    self.move(row, col, board)
                return True
            if self.first_move and self.row - row == 2 * self.direction and not board[row + self.direction][col]:
                if move:
                    self.move(row, col, board)
                return True
        
        if self.row - row == self.direction and abs(self.col - col) == 1 and board[row][col]:
            if move:
                self.move(row, col, board)
            return True
        return False
    
    def move(self, row, col, board):
        board[row][col] = self
        board[self.row][self.col] = Nothing()
        self.set_position(row, col)
        self.first_move = False
        if (self.row == 7 and self.is_white) or (self.row == 0 and not self.is_white):
            self.promote(row, col, board)

    def promote(self, row, col, board):
        while True:
            promotion_piece = input("Enter the piece you want to promote to (Q, R, B, N): ").upper()
            match promotion_piece:
                case 'Q':
                    board[row][col] = Queen(row, col, self.is_white)
                    break
                case 'R':
                    board[row][col] = Rook(row, col, self.is_white)
                    break
                case 'B':
                    board[row][col] = Bishop(row, col, self.is_white)
                    break
                case 'N':
                    board[row][col] = Knight(row, col, self.is_white)
                    break
                case _:
                    print("Invalid promotion piece.")


class King(ChessPiece):
    def __init__(self, row, col, is_white):
        super().__init__(row, col, is_white)
        self.can_castle = True

    def can_move(self, row, col, board, move=False):
        if not check_pos(row, col):
            return False
        if board[row][col] and board[row][col].is_white == self.is_white:
            return False
        if board.is_under_attack(row, col, self.is_white):
            return False

        if abs(self.row - row) <= 1 and abs(self.col - col) <= 1:
            if move:
                board[row][col] = self
                board[self.row][self.col] = Nothing()
                self.set_position(row, col)
                self.can_castle = False
                if self.is_white:
                    board.white_king_pos = (row, col)
                else:
                    board.black_king_pos = (row, col)
            return True
            
        if self.can_castle and self.row == row and move:
            if col == self.col + 2:
                rook = board[self.row][7]
                if (isinstance(rook, Rook) and rook.can_castle and
                        not board[self.row][self.col + 1] and
                        not board[self.row][self.col + 2]):
                    self.can_castle = False
                    rook.can_castle = False
                    rook.set_position(self.row, self.col + 1)
                    board[self.row][self.col + 1] = rook
                    board[self.row][7] = Nothing()
                    self.set_position(row, col)
                    board[row][col] = self
                    board[self.row][self.col] = Nothing()
                    if self.is_white:
                        board.white_king_pos = (row, col)
                    else:
                        board.black_king_pos = (row, col)
                    return True
            elif col == self.col - 2:
                rook = board[self.row][0]
                if (isinstance(rook, Rook) and rook.can_castle and 
                    not board[self.row][self.col - 1] and not board[self.row]
                        [self.col - 2] and not board[self.row][self.col - 3]):
                    self.can_castle = False
                    rook.can_castle = False
                    rook.set_position(self.row, self.col - 1)
                    board[self.row][self.col - 1] = rook
                    board[self.row][0] = Nothing()
                    board[row][col] = self
                    board[self.row][self.col] = Nothing()
                    self.set_position(row, col)
                    if self.is_white:
                        board.white_king_pos = (row, col)
                    else:
                        board.black_king_pos = (row, col)
                    return True
        return False


class Board:
    def __init__(self):
        self.field = [[Nothing() for _ in range(8)] for _ in range(8)]
        pieces = ['Rook', 'Knight', 'Bishop', 'Queen', 'King', 'Bishop', 'Knight', 'Rook']
        for i in range(8):
            self.field[0][i] = eval(pieces[i])(0, i, True)
            self.field[7][i] = eval(pieces[i])(7, i, False)
        for i in range(8):
            self.field[1][i] = Pawn(1, i, True)
            self.field[6][i] = Pawn(6, i, False)
        self.is_white_turn = True
        self.white_king_pos = (0, 4)
        self.black_king_pos = (7, 4)

    def print_board(self):
        print('     +----+----+----+----+----+----+----+----+')
        for row in range(7, -1, -1):
            print(' ', row, end='  ')
            for col in range(8):
                print('|', self.field[row][col], end=' ')
            print('|')
            print('     +----+----+----+----+----+----+----+----+')
        print(end='        ')
        for col in range(8):
            print(col, end='    ')
        print()

    def __str__(self):
        self.print_board()
        return ''

    def move_piece(self, row, col, row1, col1):
        piece = self.field[row][col]
        if piece.is_white != self.is_white_turn:
            return False
        if piece.can_move(row1, col1, self):
            test_board = self.copy()
            test_piece = piece.copy()
            test_piece.can_move(row1, col1, test_board, move=True)
            if test_board.is_white_turn and test_board.is_under_attack(*self.white_king_pos, True):
                return False
            if not test_board.is_white_turn and test_board.is_under_attack(*self.black_king_pos, False):
                return False
        if piece.can_move(row1, col1, self, move=True):
            self.is_white_turn = not self.is_white_turn
            return True
        return False
    
    def __getitem__(self, index):
        return self.field[index]
    
    def is_under_attack(self, row, col, is_white):
        for i in range(8):
            for j in range(8):
                if self.field[i][j] and self.field[i][j].is_white != is_white:
                    if self.field[i][j].can_move(row, col, self):
                        return True
        return False
    
    def get_all_possible_moves(self, is_white):
        moves = []
        test_board = self.copy()
        for row in range(8):
            for col in range(8):
                piece = test_board.field[row][col]
                if piece and piece.is_white == is_white:
                    for row1 in range(8):
                        for col1 in range(8):
                            if piece.can_move(row1, col1, test_board, move=True):
                                moves.append((row, col, row1, col1))
                                piece.can_move(row, col, test_board, move=True)
        return moves

    def is_checkmate(self, is_white):
        king_pos = self.white_king_pos if is_white else self.black_king_pos
        if not self.is_under_attack(*king_pos, is_white):
            return False

        for row, col, row1, col1 in self.get_all_possible_moves(is_white):
            test_board = self.copy()
            if test_board.field[row][col].can_move(row1, col1, test_board, move=True):
                new_king_pos = test_board.white_king_pos if is_white else test_board.black_king_pos
                if not test_board.is_under_attack(*new_king_pos, is_white):
                    return False
        return True
    
    def copy(self):
        new_board = Board()
        for row in range(8):
            for col in range(8):
                new_board.field[row][col] = self.field[row][col].copy()
        new_board.is_white_turn = self.is_white_turn
        new_board.white_king_pos = self.white_king_pos
        new_board.black_king_pos = self.black_king_pos
        return new_board


board = Board()
while True:
    print(f'Move {"white" if board.is_white_turn else "black"}:')
    board.print_board()
    print('exit - exit\nmove <row> <col> <row1> <col1> - move')
    command = input().split()
    if command[0] == 'exit':
        break
    elif command[0] == 'move':
        if board.move_piece(int(command[1]), int(command[2]), int(command[3]), int(command[4])):
            if board.is_checkmate(board.is_white_turn):
                print(f'Checkmate! {"White" if board.is_white_turn else "Black"} wins!')
                break
        else:
            print('Invalid move!')