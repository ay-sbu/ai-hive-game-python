from model.pieces import can_move
from model.pieces import piece_naming



class Board(object):

    def __init__(self):
        # the board starts with one row and a column without pieces
        self.pieces = {}
        self.black_pieces = {"queen": 1, "beetle": 2, "spider": 2, "locust": 3, "ant": 3}
        self.white_pieces = {"queen": 1, "beetle": 2, "spider": 2, "locust": 3, "ant": 3}
        self.board = [[[]]]
        self.initial_turn = True

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
        x_counter = 0
        y_counter = 0

        while x < 0 or x_counter % 2 == 1:
            self.add_column(first=True)
            x += 1
            x_counter += 1
        while x >= len(self.board[0]) or x_counter % 2 == 1:
            self.add_column()
            x_counter += 1
        while y < 0 or y_counter % 2 == 1:
            self.add_row(first=True)
            y += 1
            y_counter += 1
        while y >= len(self.board) or y_counter % 2 == 1:
            self.add_row()
            y_counter += 1
        return x, y

    def piece_in_game(self, piece):
        """ return True if piece in game """
        return piece in self.pieces.keys()

    def possible_insert(self, piece, position):
        """
        check that the piece do not insert next to other color
        """
        around_point = self.around(position)
        color = piece[0]

        flag = False
        for point in around_point:
            x, y = point
            if x >= 0 and y >= 0:
                try:
                    point_near = self.board[y][x]
                    if not point_near == []:
                        if not point_near[-1][0] == color:
                            return "the piece should not be insert next to other color"
                        else:
                            flag = True
                except:
                    pass
        if flag:
            return "ok"
        return "the piece should be insert next to its color"

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
        color = piece[0]
        if not (color + "Q1") in self.pieces:
            return "queen has not entered the game"

        # give the old position of piece
        xx, yy = self.pieces.get(piece)

        position = self.give_position(direction, ref_piece)
        x, y = self.resize(position)
        if can_move(piece, (x, y), self):
            self.board[y][x] = self.board[y][x] + [piece]
            self.pieces[piece] = (x, y)
            self.board[yy][xx].remove(piece)
            return "ok"
        return "movement is invalid"

    def insert_piece(self, piece, position, around=False, manual=False):
        if not around and not manual:
            message = self.possible_insert(piece, position)
            if not message == "ok" and not self.initial_turn:
                return message
            self.initial_turn = False
        message = "ok"
        x, y = self.resize(position)
        if self.board[y][x] == []:
            self.board[y][x] = self.board[y][x] + [piece]
            self.pieces[piece] = (x, y)
            piece_name = piece_naming(piece)
            if piece[0] == "b":
                if self.black_pieces[piece_name] > 1:
                    self.black_pieces.update({piece_name:self.black_pieces[piece_name]-1})
                else:
                    del self.black_pieces[piece_name]
            else:
                if self.white_pieces[piece_name] > 1:
                    self.white_pieces.update({piece_name:self.white_pieces[piece_name]-1})
                else:
                    del self.white_pieces[piece_name]

            return message
        return "the cell must be empty for insert"

    def end_game(self):
        try:
            white_win = True
            x, y = self.pieces["bQ1"]
            arounds = self.around((x, y))
            for neighbour in arounds:
                x, y = neighbour
                if self.board[y][x] == []:
                    white_win = False

            black_win = True
            x, y = self.pieces["wQ1"]
            arounds = self.around((x, y))
            for neighbour in arounds:
                x, y = neighbour
                if self.board[y][x] == []:
                    black_win = False
            if white_win:
                if black_win:
                    print("The game equalised")
                    return True
                print("Black lose tha game and white win")
                return True
            if black_win:
                print("White lose tha game and black win")
                return True
        except:
            pass
        return False

    def read_command(self, piece, direction, ref_piece):
        if self.piece_in_game(ref_piece):
            if self.piece_in_game(piece):
                return self.move(piece, direction, ref_piece)
            else:
                return self.insert_piece(piece, self.give_position(direction, ref_piece))
        else:
            return "ref_piece isn't in game"

    @staticmethod
    def around(position):
        """" return six point around the position as a list """

        x, y = position
        around_point = [(x + 1, y), (x - 1, y)]
        if y % 2 == 0:
            around_point.append((x, y - 1))
            around_point.append((x, y + 1))
            around_point.append((x - 1, y - 1))
            around_point.append((x - 1, y + 1))
        else:
            around_point.append((x, y - 1))
            around_point.append((x, y + 1))
            around_point.append((x + 1, y - 1))
            around_point.append((x + 1, y + 1))
        return around_point

