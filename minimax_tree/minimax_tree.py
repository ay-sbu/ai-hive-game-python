import copy
from random import random

from node import Node
from model.pieces import initial_condition_for_move, ant_move, piece_naming, beetle_move, spider_move, queen_move
from view import print_board


class MinimaxTree:
    last_depth = []
    depth_limit_checking = 3
    turn = 0

    def __init__(self, board):
        print(f'root is {board}')
        self.node = Node(board, [], None, 0)
        self.last_depth.append(self.node)
        # self.first_tree_making()

    def minimax(self, node, alpha, beta):
        if node.turn ==

    def make_tree(self, turn):

        old_last_depth = copy.deepcopy(self.last_depth)
        self.last_depth = []
        for node in old_last_depth:
            children = possible_state(node)
            if not children:
                continue
            for child in children:
                new_node = Node(child, [], node, turn + 7)
                node.children.append(new_node)
                self.last_depth.append(new_node)

    def update_last_depth(self, turn):
        node_to_expand = self.last_depth.pop()

        children = possible_state(node_to_expand)
        new_nodes = []
        for child in children:
            new_node = Node(child, [], node_to_expand, node_to_expand.turn)
            node_to_expand.children.append(new_node)
            new_nodes.append(new_node)

        new_nodes.reverse()
        self.last_depth.extend(new_nodes)

        if node_to_expand.turn + 1 != turn + self.depth_limit_checking:
            self.update_last_depth(turn)
            return

        for last_node in self.last_depth:
            if last_node.turn == turn + self.depth_limit_checking:
                last_node.score = heuristic(last_node)


            else:
                break

        print(len(self.last_depth))
        # self.print_tree()
        return self.last_depth[0].board

    def print_tree(self):
        for node in self.last_depth:
            print_board(node.board.board)
            print("\n#####################################\n")
    # def best_child(self):
    #     max = 0
    #     for node in self.last_depth:
    #         score = eval(node)
    #         if score > max:
    #             best_node = node
    #             max = score
    #
    #     return best_node
    #
    # def ai_move(self) -> string:
    #     best = self.best_child()


def possible_state(node):
    possibles_state = []
    # x = possible_movement(node, "b")
    # print(x)
    # possibles_state.extend(x)
    possibles_state.extend(possible_insert(node, "b"))
    return possibles_state


def possible_movement(node, color):
    possible_move = []
    print(node.turn)
    if "bQ1" not in node.board.pieces if color == "b" else "wQ1" not in node.board.pieces:
        return possible_move
    for piece in node.board.pieces:
        piece_position = node.board.pieces[piece]
        if not piece[0] == color:
            continue
        new_board = initial_condition_for_move(piece, node.board)
        # new_board can be False or if continuity is True should be new board

        if new_board is False:
            continue

        role = piece[1]
        if role == "Q":
            around = new_board.around(piece_position)
            for position in around:
                x, y = new_board.resize(position)
                around_around = new_board.around((x, y))
                for position_position in around_around:
                    if not new_board.board[y][x] == []:
                        if queen_move((x, y), node.board.pieces[piece], new_board, piece):
                            possible_move.append(make_state_move(new_board, piece, (x, y)))
        elif role == "B":
            around = new_board.around(piece_position)
            for position in around:
                x, y = new_board.resize(position)
                if beetle_move((x, y), node.board.pieces[piece], new_board, piece):
                    possible_move.append(make_state_move(new_board, piece, (x, y)))
        elif role == "A":
            for second_piece in new_board.pieces:
                around = new_board.around(new_board.pieces[second_piece])
                for position in around:
                    x, y = new_board.resize(position)
                    if not new_board.board[y][x] == []:
                        continue
                    if ant_move((x, y), node.board.pieces[piece], new_board, piece):
                        possible_move.append(make_state_move(new_board, piece, (x, y)))
        elif role == "S":
            possible_positions = spider_move((0, 0), node.board.pieces[piece], new_board, piece, True)
            for possible_position in possible_positions:
                possible_move.append(make_state_move(new_board, piece, possible_position))
        else:

            # locust move
            pass
        return possible_move


def possible_insert(node, color):
    possible_state = []

    if node.turn == 0:
        for possible_piece in node.board.black_pieces.keys() if color == "b" else node.board.white_pieces.keys():
            possible_state.append(make_state_insert(node.board, possible_piece, (0, 0), color))
        return possible_state
    if node.turn == 1:
        for possible_piece in node.board.black_pieces.keys() if color == "b" else node.board.white_pieces.keys():
            possible_state.append(make_state_insert(node.board, possible_piece, (1, 0), color))

        return possible_state

    flag = False
    if (node.turn == 7 or node.turn == 6) and not (color + "Q1") in node.board.pieces:
        flag = True

    for piece in node.board.pieces:
        if piece[0] == 'w' if color == "b" else "b":
            continue
        around = node.board.around(node.board.pieces[piece])
        for position in around:
            x, y = node.board.resize(position)
            if not node.board.board[y][x] == []:
                continue
            if node.board.possible_insert(piece, position) == "ok":
                if flag:
                    possible_state.append(make_state_insert(node.board, "queen", position, color))
                    return possible_state

                for possible_piece in node.board.black_pieces.keys() if color == "b" else node.board.white_pieces.keys():
                    possible_state.append(make_state_insert(node.board, possible_piece, position, color))

    return possible_state


def make_state_move(board, piece, position):
    state = copy.deepcopy(board)
    x, y = (position)

    state.board[y][x] = board.board[y][x] + [piece]
    state.pieces[piece] = (x, y)

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
    return int(random() * 10)
