import copy


def can_move(piece, des_position, board):
    # it can be 'A', 'B', 'L', 'Q', 'S'
    piece_role = piece[1]
    new_board = copy.deepcopy(board)

    x, y = new_board.pieces.get(piece)  # old position of the piece

    if not new_board.board[y][x][-1] == piece:
        return False

    new_board.board[y][x].remove(piece)
    del new_board.pieces[piece]

    if new_board.board[y][x] == []:
        if not check_continuity(new_board, (x, y)):
            return False

    if piece_role == 'A':
        return ant_move()
    # elif piece_role == 'B':
    #     return beetle_move(piece, position)
    # elif piece_role == 'L':
    #     return locust_move(piece, position)
    # elif piece_role == 'Q':
    #     return queen_move(piece, position)
    # elif piece_role == 'S':
    #     return spider_move(piece, position)
    # else:
    #     print("something wrong")
    #     return False



def check_continuity(board, position):
    traverse(position, board)
    if len(board.pieces) == 0:
        return True
    return False


def traverse(position, board):
    from model.board import around
    arounds = around(position)
    for neighbour in arounds:
        x, y = neighbour
        pieces = []
        if x < 0 or y < 0:
            continue
        try:
            pieces = board.board[y][x]
            board.board[y][x] = []
        except:
            pass
        if not pieces == []:
            for piece in pieces:
                del board.pieces[piece]
            traverse(neighbour, board)


def ant_move():
    return True


def beetle_move(piece, position, board):
    pass


def locust_move(piece, position, board):
    pass


def queen_move(piece, position, board):
    pass


def spider_move(piece, position):
    pass


def check_surrounding():
    




