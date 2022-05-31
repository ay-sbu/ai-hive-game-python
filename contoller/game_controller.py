from minimax_tree.minimax_tree import MinimaxTree
from view import print_board
from model.board import Board
import copy



class GameController:
    turn = 0
    b = Board()
    minimax = MinimaxTree(b)

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


    def ai_turn(self, color="b"):

        print("\n------- HiveGame ------- ")
        print("$ turn : ", end='')
        print("white") if color == "w" else print("black")
        print("$ AI : ")

        self.b = self.minimax.make_and_update_last_depth()


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
