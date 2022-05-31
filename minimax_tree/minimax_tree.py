import copy
import string
from minimax_tree.node import Node


class MinimaxTree:
    last_depth = []
    depth_limit_checking = 7

    def __init__(self, root):
        print(f'root is {root}')
        self.root = root
        self.last_depth.append(root)
        self.first_tree_making()

    def first_tree_making(self):

        for _ in range(self.depth_limit_checking):
            self.make_and_update_last_depth()

    def make_and_update_last_depth(self):
        old_last_depth = copy.deepcopy(self.last_depth)
        self.last_depth = []
        for node in old_last_depth:
            nodes = possible_nodes(node)
            if nodes == []:
                continue
            node.children = nodes
            self.last_depth.append(node)
        return True

    def best_child(self):
        max = 0
        for node in self.last_depth:
            score = eval(node)
            if score > max:
                best_node = node
                max = score

        return best_node

    def ai_move(self) -> string:
        best = self.best_child()


def possible_nodes(board):
    pass


def eval(board):
    return len(board)


def possible_movement(self):
    pass


def possible_insert(self, color):
    possible_state = []

    if self.turn == 0:
        for possible_piece in self.b.black_pieces.keys() if color == "b" else self.b.white_pieces.keys():
            possible_state.append(self.make_state(possible_piece, (0, 0), color))
            return possible_state
    if self.turn == 1:
        for possible_piece in self.b.black_pieces.keys() if color == "b" else self.b.white_pieces.keys():
            possible_state.append(self.make_state(possible_piece, (1, 0), color))

        return possible_state

    flag = False
    if (self.turn == 7 or self.turn == 6) and not (color + "Q1") in self.b.pieces:
        flag = True

    for piece in self.b.pieces:
        if piece[0] == 'w' if color == "b" else "b":
            continue
        around = self.b.around(self.b.pieces[piece])
        for position in around:
            x, y = self.b.resize(position)
            if not self.b.board[y][x] == []:
                continue
            if self.b.possible_insert(piece, position) == "ok":
                if flag:
                    possible_state.append(self.make_state("queen", position, color))
                    return possible_state

                for possible_piece in self.b.black_pieces.keys() if color == "b" else self.b.white_pieces.keys():
                    possible_state.append(self.make_state(possible_piece, position, color))

    return possible_state


def make_state(self, piece_name, position, color):
    state = copy.deepcopy(self.b)
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
