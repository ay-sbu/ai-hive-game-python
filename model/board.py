from model.pieces import can_move


def around(position):
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

    def piece_in_game(self, piece):
        """ return True if piece in game """
        return piece in self.pieces.keys()

    @staticmethod
    def around(position):
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

    def possible_insert(self, piece, position):
        around_point = self.around(position)
        color = piece[0]
        flag = False
        for point in around_point:
            x, y = point
            try:
                point_near = self.board[y][x][0]
                if not point_near == []:
                    if not point_near[0] == color:
                        return "the piece should not be next to other color"
                    else:
                        flag = True
            except:
                pass
        if flag:
            return "ok"
        return "the piece should be next to its color"

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
        x,y = position

        if can_move(piece, position, self):
            self.board[y][x] = self.board[y][x] + [piece]
            self.pieces[piece] = (x, y)
            self.board[y][x].remove(piece)
            return "ok"
        return "movement is invalid"

    def insert_piece(self, piece, position):
        flag = self.possible_insert(piece, position)
        if not flag == "ok":
            return flag
        x, y = self.resize(position)
        self.board[y][x] = self.board[y][x] + [piece]
        self.pieces[piece] = (x, y)
        return flag

    def read_command(self, piece, direction, ref_piece):
        if self.piece_in_game(ref_piece):
            if self.piece_in_game(piece):
                return self.move(piece, direction, ref_piece)
            else:
                return self.insert_piece(piece, self.give_position(direction, ref_piece))
        else:
            return "ref_piece isn't in game"
