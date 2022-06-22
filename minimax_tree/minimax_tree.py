import copy


from view import print_board
from random import random
from minimax_tree.node import Node
from model.pieces import around, check_continuity, initial_condition_for_move, ant_move, piece_naming, beetle_move, \
    spider_move, queen_move

MIN = -100
MAX = -MIN


class MinimaxTree:
    depth_limit_checking = 2

    def __init__(self, board):
        self.root = Node(board, [], None, 0)
        self.next_state = None
        self.this_turn = 0

    def minimax(self, node, alpha, beta):
        flag = False
        if self.root == node:
            flag = True

        if node.turn == self.this_turn + self.depth_limit_checking:
            # print_board(node.board.board)
            return heuristic(node)

        if not node.children:
            update_last_depth(node)
        #
        # print("################################")
        # for child in node.children:
        #
        #     print_board(child.board.board)

        if node.turn % 2 == 0:  # maximizing player

            best = MIN

            for child in node.children:
                val = self.minimax(child, alpha, beta)
                if flag and val > best:
                    self.next_state = child
                best = max(best, val)
                alpha = max(alpha, best)

                # Alpha Beta Pruning
                if beta <= alpha:
                    break

            return best

        else:  # minimizing player

            best = MAX

            for child in node.children:
                val = self.minimax(child, alpha, beta)
                if flag and val < best:
                    self.next_state = child
                best = min(best, val)
                beta = min(beta, best)

                # Alpha Beta Pruning
                if beta <= alpha:
                    break

            return best

    def give_next_state(self):
        self.this_turn += 1
        self.minimax(self.root, MIN, MAX)
        self.root = self.next_state
        return self.next_state.board

    def update_root(self, board):
        self.this_turn += 1

        for child in self.root.children:
            if child.board == board:  # todo: check '==' for compare two board object
                self.root = child
                return

        self.root = Node(board, [], None, self.root.turn + 1)


def update_last_depth(node):
    if node.turn % 2 == 0:
        children = possible_state(node, "b")
    else:
        children = possible_state(node, "w")

    new_nodes = []
    for child in children:
        new_node = Node(child, [], node, node.turn + 1)
        node.children.append(new_node)
        new_nodes.append(new_node)
    return new_nodes


def possible_state(node, color):
    possibles_state = []
    possibles_state.extend(possible_movement(node, color))
    possibles_state.extend(possible_insert(node, color))
    return possibles_state


def possible_movement(node, color):
    possible_move = []

    if ("bQ1" if color == "b" else "wQ1") not in node.board.pieces:
        return possible_move
    for piece in node.board.pieces:
        if not piece[0] == color:
            continue

        piece_position = node.board.pieces[piece]
        new_board = initial_condition_for_move(piece, node.board)
        # new_board can be False or if continuity is True should be new board

        if new_board is False:
            continue

        role = piece[1]

        if role == "Q":
            around = new_board.around(piece_position)
            for position in around:
                x, y = position
                around_around = new_board.around((x, y))

                for position_position in around_around:
                    xx, yy = position_position
                    try:
                        if not new_board.board[yy][xx] == []:
                            if queen_move((x, y), piece_position, new_board, piece):
                                possible_move.append(make_state_move(new_board, piece, (x, y)))
                    except:
                        pass

        elif role == "B":
            around = new_board.around(piece_position)
            for position in around:
                x, y = position
                around_around = new_board.around((x, y))

                for position_position in around_around:
                    xx, yy = position_position
                    try:
                        if not new_board.board[yy][xx] == []:
                            if beetle_move((x, y), piece_position, new_board, piece):
                                possible_move.append(make_state_move(new_board, piece, (x, y)))
                    except:
                        pass
        elif role == "A":
            for second_piece in new_board.pieces:
                around = new_board.around(new_board.pieces[second_piece])
                for position in around:
                    x, y = position
                    if not new_board.board[y][x] == []:
                        continue
                    if ant_move((x, y), node.board.pieces[piece], new_board, piece):
                        possible_move.append(make_state_move(new_board, piece, (x, y)))
        elif role == "S":
            possible_positions = spider_move((0, 0), node.board.pieces[piece], new_board, piece, True)
            for possible_position in possible_positions:
                possible_move.append(make_state_move(new_board, piece, possible_position))

        # locust_possible_moves 6 direction(y/x): (no/l) (no/r) (l/l) (l/r) (r/l) (r/r) 
        # we move the locust by 6 whiles
        else:
            # no/l
            x, y = piece_position
            if new_board.board[y][x - 1] != []:
                x -= 1
                while True:
                    x -= 1
                    if new_board.board[y][x] == []:
                        possible_position = (x, y)
                        possible_move.append(make_state_move(new_board, piece, possible_position))
                        break

            # no/r
            x, y = piece_position
            if new_board.board[y][x + 1] != []:
                x += 1
                while True:
                    x += 1
                    try:
                        if new_board.board[y][x] == []:
                            possible_position = (x, y)
                            possible_move.append(make_state_move(new_board, piece, possible_position))
                            break
                    except:
                        print_board(node.parent.board.board)
                        print()
                        print_board(node.board.board)
                        print()
                        print_board(new_board.board)
                        return
            # l/l
            x, y = piece_position
            if new_board.board[y - 1][(x - 1) if y % 2 == 1 else x] != []:
                y -= 1
                if y % 2 == 1:
                    x -= 1
                while True:
                    y -= 1
                    if y % 2 == 1:
                        x -= 1
                    if new_board.board[y][x] == []:
                        possible_position = (x, y)
                        possible_move.append(make_state_move(new_board, piece, possible_position))
                        break

            # l/r
            x, y = piece_position
            if new_board.board[y - 1][(x + 1) if y % 2 == 1 else x] != []:
                y -= 1
                if y % 2 == 1:
                    x += 1
                while True:
                    y -= 1
                    if y % 2 == 1:
                        x += 1
                    if new_board.board[y][x] == []:
                        possible_position = (x, y)
                        possible_move.append(make_state_move(new_board, piece, possible_position))
                        break

            # r/l
            x, y = piece_position
            if new_board.board[y + 1][(x - 1) if y % 2 == 0 else x] != []:
                y += 1
                if y % 2 == 0:
                    x -= 1
                while True:
                    y += 1
                    if y % 2 == 0:
                        x -= 1
                    try:
                        if new_board.board[y][x] == []:
                            possible_position = (x, y)
                            possible_move.append(make_state_move(new_board, piece, possible_position))
                            break
                    except:
                        print_board(node.parent.board.board)
                        print()
                        print_board(node.board.board)
                        print()
                        print_board(new_board.board)
                        return
                        # r/r
            x, y = piece_position
            if new_board.board[y + 1][(x + 1) if y % 2 == 0 else x] != []:
                y += 1
                if y % 2 == 0:
                    x += 1
                while True:
                    y += 1
                    if y % 2 == 0:
                        x += 1
                    if new_board.board[y][x] == []:
                        possible_position = (x, y)
                        possible_move.append(make_state_move(new_board, piece, possible_position))
                        break

    return possible_move


def possible_insert(node, color):
    possible_state = []

    if node.turn == 0:
        for possible_piece in (node.board.black_pieces.keys() if color == "b" else node.board.white_pieces.keys()):
            possible_state.append(make_state_insert(node.board, possible_piece, (1, 1), color))

        return possible_state

    flag = False
    if (node.turn == 7 or node.turn == 6) and not (color + "Q1") in node.board.pieces:
        flag = True

    for piece in node.board.pieces:
        if piece[0] == ('w' if color == "b" else "b"):
            continue
        around = node.board.around(node.board.pieces[piece])
        for position in around:
            x, y = position
            if not node.board.board[y][x] == []:
                continue
            if node.board.possible_insert(piece, position) == "ok":
                if flag:
                    possible_state.append(make_state_insert(node.board, "queen", position, color))
                    return possible_state

                for possible_piece in (node.board.black_pieces.keys() if color == "b" else node.board.white_pieces.keys()):
                    possible_state.append(make_state_insert(node.board, possible_piece, position, color))

    return possible_state


def make_state_move(board, piece, position):

    state = copy.deepcopy(board)
    x, y = position

    state.board[y][x] = state.board[y][x] + [piece]
    state.pieces[piece] = (x, y)
    state.resize_page(x,y)


    return state


def make_state_insert(board, piece_name, position, color):
    state = copy.deepcopy(board)
    if piece_name == "ant":
        if color + "A1" in state.pieces.keys():
            if color + "A2" in state.pieces.keys():
                state.insert_piece(color + "A3", position, True, True)
            else:
                state.insert_piece(color + "A2", position, True, True)
        else:
            state.insert_piece(color + "A1", position, True, True)
    elif piece_name == "locust":
        if color + "L1" in state.pieces.keys():
            if color + "L2" in state.pieces.keys():
                state.insert_piece(color + "L3", position, True, True)
            else:
                state.insert_piece(color + "L2", position, True, True)
        else:
            state.insert_piece(color + "L1", position, True, True)
    elif piece_name == "spider":
        if color + "S1" in state.pieces.keys():
            state.insert_piece(color + "S2", position, True, True)
        else:
            state.insert_piece(color + "S1", position, True, True)
    elif piece_name == "beetle":
        if color + "B1" in state.pieces.keys():
            state.insert_piece(color + "B2", position, True, True)
        else:
            state.insert_piece(color + "B1", position, True, True)
    else:
        state.insert_piece(color + "Q1", position, True, True)

    return state


def heuristic(node):
    
    if "bQ1" in node.board.pieces:
        return 90
    
    if "wQ1" in node.board.pieces:
        around_white_queen = len(around(node.board.pieces.get("wQ1")))
    else:
        around_white_queen = 0
    if "bQ1" in node.board.pieces:
        around_black_queen = len(around(node.board.pieces.get("bQ1")))
    else:
        around_black_queen = 0
    p1 = around_black_queen - around_white_queen
    c1 = 10
    
    white_active_ants = active_ants_count(node, 'w')
    black_active_ants = active_ants_count(node, 'b')
    p2 = white_active_ants - black_active_ants
    c2 = 5
    
    try:
        white_in_game_ants = 3 - node.board.white_pieces["ant"]
    except Exception:
        white_in_game_ants = 3
    
    try:
        black_in_game_ants = 3 - node.board.black_pieces["ant"]
    except Exception:
        black_in_game_ants = 3
    p3 = white_in_game_ants - black_in_game_ants
    c3 = 30
    
    white_locusts_possible_moves = locusts_moves_counts(node, 'w')
    black_locusts_possible_moves = locusts_moves_counts(node, 'b')
    p4 = white_locusts_possible_moves - black_locusts_possible_moves
    c4 = 2
    
    
    # spider is a stupid piece, so we don't consider it :)
    
    score = (c1 * p1) + (c2 * p2) + (c3 * p3) + (c4 * p4)
    
    return -score

    # return int(random() * 10)


# todo: I think possible_movement can be decompose to checking each piece
def locusts_moves_counts(node, color):
    possible_move = []
    for piece in node.board.pieces:
        if piece[0] != color or piece[1] != "L":
            continue

        piece_position = node.board.pieces[piece]
        new_board = initial_condition_for_move(piece, node.board)
        # new_board can be False or if continuity is True should be new board

        if new_board is False:
            continue

        x, y = piece_position
        if new_board.board[y][x - 1] != []:
            x -= 1
            while True:
                x -= 1
                if new_board.board[y][x] == []:
                    possible_position = (x, y)
                    possible_move.append(make_state_move(new_board, piece, possible_position))
                    break

        # no/r
        x, y = piece_position
        if new_board.board[y][x + 1] != []:
            x += 1
            while True:
                x += 1
                if new_board.board[y][x] == []:
                    possible_position = (x, y)
                    possible_move.append(make_state_move(new_board, piece, possible_position))
                    break

        # l/l
        x, y = piece_position
        if new_board.board[y - 1][(x - 1) if y % 2 == 1 else x] != []:
            y -= 1
            if y % 2 == 1:
                x -= 1
            while True:
                y -= 1
                if y % 2 == 1:
                    x -= 1
                if new_board.board[y][x] == []:
                    possible_position = (x, y)
                    possible_move.append(make_state_move(new_board, piece, possible_position))
                    break

        # l/r
        x, y = piece_position
        if new_board.board[y - 1][(x + 1) if y % 2 == 1 else x] != []:
            y -= 1
            if y % 2 == 1:
                x += 1
            while True:
                y -= 1
                if y % 2 == 1:
                    x += 1
                if new_board.board[y][x] == []:
                    possible_position = (x, y)
                    possible_move.append(make_state_move(new_board, piece, possible_position))
                    break

        # r/l
        x, y = piece_position
        if new_board.board[y + 1][(x - 1) if y % 2 == 0 else x] != []:
            y += 1
            if y % 2 == 0:
                x -= 1
            while True:
                y += 1
                if y % 2 == 0:
                    x -= 1
                if new_board.board[y][x] == []:
                    possible_position = (x, y)
                    possible_move.append(make_state_move(new_board, piece, possible_position))
                    break

        # r/r
        x, y = piece_position
        if new_board.board[y + 1][(x + 1) if y % 2 == 0 else x] != []:
            y += 1
            if y % 2 == 0:
                x += 1
            while True:
                y += 1
                if y % 2 == 0:
                    x += 1
                if new_board.board[y][x] == []:
                    possible_position = (x, y)
                    possible_move.append(make_state_move(new_board, piece, possible_position))
                    break

    return len(possible_move)


def active_ants_count(node, color):
    possibles = 0
    for piece in node.board.pieces:
        if piece[0] != color or piece[1] != "A":
            continue

        if check_continuity(node.board, node.board.pieces[piece]):
            possibles += 1

    return possibles
