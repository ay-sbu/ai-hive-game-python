class Board(object):

    def __init__(self):
        # the board starts with one row and a column without pieces
        self.pieces = {}
        self.board = [[[]]]


    def add_row(self, first=False):
        new_row = []
        row_size = len(self.board[0])
        for i in range(row_size):
            new_row.append([])
        if first:
            self.board.insert(0, new_row)
            for key in self.pieces.keys():
                x, y = self.pieces[key]
                y += 1
                self.pieces[key] = x, y
        else:
            self.board.append(new_row)

    def add_column(self, first=False):
        if first:
            for key in self.pieces.keys():
                x, y = self.pieces[key]
                x += 1
                self.pieces[key] = x, y
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

    def insert_piece(self, piece, position):
        x,y = self.resize(position)
        # TODO : check that position is free or piece is beetle
        self.board[y][x] = self.board[y][x] + [piece]
        self.pieces[piece] = (x,y)

    def piece_in_game(self, piece):
        """ return True if piece in game """
        return piece in self.pieces.keys()

    def give_position(self, direction, piece):
        """ return the position of direction than piece """
        x, y = self.pieces[piece]
        if direction == "e":
            return x + 1, y
        elif direction == "w":
            return x - 1, y
        if y % 2 == 0:
            if direction == "ne":
                return x, y - 1
            elif direction == "se":
                return x, y + 1
            elif direction == "nw":
                return x - 1, y - 1
            else:
                return x - 1, y + 1
        else:
            if direction == "nw":
                return x, y - 1
            elif direction == "sw":
                return x, y + 1
            elif direction == "ne":
                return x + 1, y - 1
            else:
                return x + 1, y + 1

    def move(self, piece, direction, ref_piece):
        position = self.give_position(direction, ref_piece)
        # TODO : check that

    def read_command(self, piece, direction, ref_piece):
        if self.piece_in_game(ref_piece):
            if self.piece_in_game(piece):
                self.move(piece, direction, ref_piece)
            else:
                self.insert_piece(piece, self.give_position(direction, ref_piece))
        else:
            return "ref_piece isn't in game"
