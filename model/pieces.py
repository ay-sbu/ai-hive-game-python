import copy
from ctypes import resize
import model.board
from shutil import move


def around(position):
    x, y = position
    around_point = [(x + 1, y)]
    if y % 2 == 0:
        around_point.append((x, y + 1))
        around_point.append((x - 1, y + 1))
        around_point.append((x - 1, y))
        around_point.append((x - 1, y - 1))
        around_point.append((x, y - 1))
    else:
        around_point.append((x + 1, y + 1))
        around_point.append((x, y + 1))
        around_point.append((x - 1, y))
        around_point.append((x, y - 1))
        around_point.append((x + 1, y - 1))
    return around_point


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
        return ant_move(des_position, (x, y), new_board, piece)
    elif piece_role == 'B':
        return beetle_move(des_position, (x, y), new_board, piece)
    elif piece_role == 'L':
        return locust_move(des_position, (x, y), board, piece)
    elif piece_role == 'Q':
        return queen_move(des_position, (x, y), new_board, piece)
    elif piece_role == 'S':
        return spider_move(des_position, (x, y), new_board, piece)
    else:
        print("something wrong")
        return False


def check_continuity(board, position):
    traverse(position, board)
    if len(board.pieces) == 0:
        return True
    return False


def traverse(position, board):
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


def ant_move(des_position, position, board, piece):
    x, y = des_position
    if board.board[y][x] == []:
        if check_surrounding(des_position, board, piece) \
                and check_surrounding(position, board, piece):
            return True
    return False


def beetle_move(des_position, position, board, piece):
    x, y = des_position
    if des_position in around(position):
        if board.board[y][x] == []:
            if check_surrounding(des_position, board, piece) \
                    and check_surrounding(position, board, piece):
                return True
        else:
            return True
    return False


def locust_move(des_position, position, board, piece):
    pos_x, pos_y = position
    x, y = position
    des_x, des_y = des_position

    # locust can't go to his arounds
    if abs(x - des_x) <= 1 and \
            abs(y - des_y) <= 1:
        return False

    # find move direction
    y_direction = ''
    x_direction = ''
    if y == des_y:
        y_direction = 'no'
    elif y < des_y:
        y_direction = 'r'
    else:
        y_direction = 'l'

    if x == des_x:
        return False
    elif x < des_x:
        x_direction = 'r'
    elif x > des_x:
        x_direction = 'l'

    # locust should insert in first blank position

    # move position to des_position Loop
    while True:
        print("here", f'{y}, {x}')
        if y == des_y and x == des_x:
            board.board[pos_y][pos_x].remove(piece)
            board.board[y][x].append(piece)
            return True
        
        if board.board[y][x] == []:
            return False

        # no_direction for y
        if y_direction == 'no':

            if x_direction == 'r':

                x += 1

                if x > des_x:
                    return False

            else:

                x -= 1

                if x < des_x:
                    return False

        elif y_direction == 'r':

            y += 1

            if y > des_y:
                return False

            if y % 2 == 0:
                if x_direction == 'r':
                    x += 1

                    if x > des_x:
                        return False

                else:

                    x -= 1

                    if x < des_x:
                        return False

        else:

            y -= 1

            if y < des_y:
                return False

            if y % 2 == 1:
                if x_direction == 'r':

                    x += 1

                    if x > des_x:
                        return False

                else:

                    x -= 1

                    if x < des_x:
                        return False


def queen_move(des_position, position, board, piece):
    x, y = des_position
    if des_position in around(position):
        if board.board[y][x] == []:
            if check_surrounding(des_position, board, piece) \
                    and check_surrounding(position, board, piece):
                return True
    return False


def spider_move(des_position, position, board, piece):
    arounds = around(position)
    first = []
    if check_surrounding(position, board, piece):
        for around_point in arounds:
            if spider_checking(around_point, board, piece):
                first.append(around_point)

    second = []
    for i in first:
        arounds = around(i)
        for around_point in arounds:
            if spider_checking(around_point, board, piece) and not around_point in first:
                second.append(around_point)

    third = []
    for i in second:
        arounds = around(i)
        for around_point in arounds:
            if spider_checking(around_point, board, piece) and not around_point in second:
                third.append(around_point)

    return des_position in third



def spider_checking(des_position, board, piece):
    x, y = des_position
    if board.board[y][x] == []:
        if check_surrounding(des_position, board, piece):
            around_des = around(des_position)
            for point in around_des:
                xx, yy = point
                if not board.board[yy][xx] == []:
                    return True
    return False


def check_surrounding(position, board, piece):
    arounds = around(position)
    for i in range(0, 3):
        x, y = arounds[i * 2]
        if board.board[y][x] == [] or board.board[y][x][-1] == piece:
            x, y = arounds[(i * 2) + 1]
            if board.board[y][x] == [] or board.board[y][x][-1] == piece:
                return True
            x, y = arounds[(i * 2) - 1]
            if board.board[y][x] == [] or board.board[y][x][-1] == piece:
                return True
    return False
