

class Board(object):

    def __init__(self):
        # the board starts with one row and a column without pieces
        self.pieces = []
        self.board = [[[]]]
        self.x = 0
        self.y = 0

    def add_row(self, first=False):
        new_row = []
        row_size = len(self.board[0])
        for i in range(row_size):
            new_row.append([])
        if first:
            self.y += 1
            self.board.insert(0, new_row)
        else:
            self.board.append(new_row)


    def add_column(self, first=False):
        if first:
            self.x += 1
            for row in self.board:
                row.insert(0, [])
        else:
            for row in self.board:
                row.append([])



    def resize(self, position):
        """
        Resizes the board to include the position (x, y)
        returns the normalized (x, y)
        """
        (x, y) = position

        while x < 0:
            self.add_column(first=True)
            x += 1
        while x >= len(self.board[0]):
            self.add_column()
        while y < 0:
            self.add_row(first=True)
            y += 1
        while y >= len(self.board):
            self.add_row()
        return x, y



    def insert_piece (self, piece, position):
        x, y = position
        self.resize(position)
        # TODO : check that position is free or piece is beetle
        self.board[y][x] = self.board[y][x] + [piece]
        self.pieces.append(piece)

    def piece_in_game(self, piece):
        """ return True if piece in game """
        return piece in self.pieces