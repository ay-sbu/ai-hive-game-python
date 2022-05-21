from view import print_board
from model.board import Board
import copy



class GameController:
    turn = 0
    b = Board()

    def start(self):

        # first command input
        self.print_menu()
        command = input()

        if command == "break":
            self.good_bye()

        if not self.check_first_command_format(command):
            self.good_bye()

        command.strip()
        self.b.insert_piece(command, (0,0), True, True)

        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1

        print_board(self.b.board)

        # Game Loop
        while True:

            if self.turn % 2 == 0:
                self.print_menu()

                command = input()

                if command == "break":
                    self.good_bye()

                if not self.check_command_format(command):
                    continue

                commands = command.split(" ")

                if self.turn == 6 and not "wQ1" in self.b.pieces and not commands[0][1] == "Q":
                    print("queen must entered in game before 5th turn")
                    continue

                massage = self.b.read_command(commands[0], commands[1], commands[2])
                print(massage)
                if self.b.end_game():
                    break
                if not massage == "ok":
                    continue

                self.turn += 1

                # print(b.board)
                # print(b.pieces)

                print_board(self.b.board)

            else:
                self.ai_turn()
                self.turn += 1

                # print(b.board)
                # print(b.pieces)

                print_board(self.b.board)


    def ai_turn(self):
        possible_state = []
        possible_state = self.possible_insert("b")
        self.b = possible_state[0]


    def possible_movement(self):
        pass

    def possible_insert(self, color):
        possible_state = []


        if self.turn == 0:
            for possible_piece in self.b.black_pieces.keys() if color == "b" else self.b.white_pieces.keys():
                possible_state.append(self.make_state(possible_piece, (0,0), color))
                return possible_state
        if self.turn == 1:
            for possible_piece in self.b.black_pieces.keys() if color == "b" else self.b.white_pieces.keys():
                possible_state.append(self.make_state(possible_piece, (1, 0), color))

            return possible_state

        flag = False
        if (self.turn == 7 or self.turn == 6) and not (color+"Q1") in self.b.pieces:
            flag = True

        for piece in self.b.pieces:
            if piece[0] == 'w' if color == "b" else "b":
                continue
            around = self.b.around(self.b.pieces[piece])
            for position in around:
                x, y = position
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
            if color+"A1" in state.pieces.keys():
                if color+"A2" in state.pieces.keys():
                    state.insert_piece(color + "A3", position, True, True)
                else:
                    state.insert_piece(color + "A2", position, True, True)
            else:
                state.insert_piece(color + "A1", position, True, True)
        elif piece_name == "locust":
            if color+"L1" in state.pieces.keys():
                if color+"L2" in state.pieces.keys():
                    state.insert_piece(color + "L3", position, True, True)
                else:
                    state.insert_piece(color + "L2", position, True, True)
            else:
                state.insert_piece(color + "L1", position, True, True)
        elif piece_name == "spider":
            if color+"S1" in state.pieces.keys():
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
        print
        return state


    def print_menu(self):
        print("\n")
        print("------- HiveGame ------- ")
        print("$ turn : ", end='')
        if self.turn % 2 == 0:
            print("white")
        else:
            print("black")

        print("$ input your command > ", end='')

    def check_command_format(self, command):
        commands = command.split()
        if len(commands) != 3 or not self.check_node_format(commands[0]) or \
                not self.check_place_format(commands[1]) or not self.check_node_format(commands[2]) or \
                self.bad_turn(commands[0][0]):
            print("bad input format!")
            return False

        return True

    def check_first_command_format(self, command):
        commands = command.split()
        if len(commands) != 1 or not self.check_node_format(command) or self.bad_turn(command[0]):
            print("bad input format!")
            return False
        return True

    def bad_turn(self, color):
        if self.turn % 2 == 0 and color == 'b':
            return True

        if self.turn % 2 == 1 and color == 'w':
            return True

        return False

    @staticmethod
    def good_bye():
        print("Good Bye!")
        exit()

    @staticmethod
    def check_place_format(string_place):
        if string_place == 'up' or \
                string_place == 'w' or \
                string_place == 'nw' or \
                string_place == 'ne' or \
                string_place == 'e' or \
                string_place == 'se' or \
                string_place == 'sw':
            return True
        return False

    @staticmethod
    def check_node_format(string_node):
        if (string_node[0] != 'w' and string_node[0] != 'b') or len(string_node) != 3:
            return False

        if string_node[1] != 'B' and \
                string_node[1] != 'Q' and \
                string_node[1] != 'L' and \
                string_node[1] != 'S' and \
                string_node[1] != 'A':
            return False

        if string_node[1] == 'L' and string_node[1] == 'A':
            if int(string_node[2]) > 3:
                return False

        if string_node[1] == 'S' and string_node[1] == 'B':
            if int(string_node[2]) > 2:
                return False

        if string_node[1] == 'Q':
            if int(string_node[2]) > 1:
                return False

        return True
