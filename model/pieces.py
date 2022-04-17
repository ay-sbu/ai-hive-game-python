
#
# class Pieces(object):
#
#     def __init__(self, color, role, num):
#         self.color = color  # can be 'b' or 'w'
#         self.number = num  # can be [1, 2, 3]
#         self.role = role  # one of ['A', 'B', 'L', 'Q', 'S']





def can_move(piece, position):
    # it can be 'A', 'B', 'L', 'Q', 'S'
    piece_role = piece[1]
    if piece_role == 'A':
        ant_move(piece, position)
    elif piece_role == 'B':
        beetle_move(piece, position)
    elif piece_role == 'L':
        locust_move(piece, position)
    elif piece_role == 'Q':
        queen_move(piece, position)
    else:
        spider_move(piece, position)


def ant_move(piece, position):
    pass


def beetle_move(piece, position):
    pass


def locust_move(piece, position):
    pass


def queen_move(piece, position):
    pass


def spider_move(piece, position):
    pass