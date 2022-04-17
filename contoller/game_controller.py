import string

from model.board import Board


def good_bye():
    print("Good Bye!")
    exit()


def print_menu():
    print("\n")
    print(" ------- HiveGame ------- ")
    print("input your command: ", end='')


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


def check_first_command_format(command, turn):
    commands = command.split()
    if len(commands) != 1 or not check_node_format(command) or bad_turn(command[0], turn):
        print("bad input format!")
        return False
    return True


def bad_turn(color, turn):
    if turn == 0 and color == 'b':
        return True

    if turn == 1 and color == 'w':
        return True

    return False


def check_command_format(command, turn):
    commands = command.split()
    if len(commands) != 3 or not check_node_format(commands[0]) or \
            not check_place_format(commands[1]) or not check_node_format(commands[2]) or \
            bad_turn(commands[0][0], turn):
        print("bad input format!")
        return False

    return True


class GameController:

    def start(self):

        b = Board()
        turn = 0

        # first command input
        print_menu()

        command = input()

        if command == "break":
            good_bye()

        if not check_first_command_format(command, turn):
            good_bye()

        command.strip()
        b.board[0][0] = b.board[0][0] + [command]
        b.pieces[command] = (0,0)

        if turn == 1:
            turn = 0
        else:
            turn = 1

        # Game Loop
        while True:
            print_menu()

            command = input()

            if command == "break":
                good_bye()

            if not check_command_format(command, turn):
                continue

            commands = command.split(" ")
            b.read_command(commands[0],commands[1],commands[2])

            print("After checking :) command sounds ok")

            if turn == 1:
                turn = 0
            else:
                turn = 1

            print(b.board)
            print(b.pieces)