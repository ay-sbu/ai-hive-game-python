import copy
from minimax_tree.minimax_tree import MinimaxTree
from view import print_board
from model.board import Board
import sys


class GameController:
    turn = 0

    def start(self):
        b = Board()
        agent_turn = 0
        tree = MinimaxTree(copy.deepcopy(b))

        # first command input
        self.print_menu()
        command = input()

        if command == "break":
            self.good_bye()

        if not self.check_first_command_format(command):
            self.good_bye()

        command.strip()
        b.board[0][0] = b.board[0][0] + [command]
        b.pieces[command] = (0, 0)

        # todo self.turn += 1
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1

        print_board(b.board)

        # Game Loop
        while True:
            self.print_menu()

            if self.turn % 2 == agent_turn:
                command = tree.ai_move()
            else:
                command = input()

            if command == "break":
                self.good_bye()

            if not self.check_command_format(command):
                continue

            commands = command.split(" ")

            if self.turn == 6 and "wQ1" not in b.pieces and commands[0][1] != "Q":
                print("queen must entered in game before 5th turn")
                continue
            if self.turn == 7 and "bQ1" not in b.pieces and commands[0][1] != "Q":
                print("queen must entered in game before 5th turn")
                continue

            massage = b.read_command(commands[0], commands[1], commands[2])
            print(massage)
            if b.end_game():
                break
            if massage != "ok":
                continue

            self.turn += 1

            print_board(b.board)

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

        if string_node[1] == 'Q' and int(string_node[2]) > 1:
                return False

        return True


def main():
    game_controller = GameController()
    game_controller.start()


if __name__ == '__main__':
    sys.exit(main())
