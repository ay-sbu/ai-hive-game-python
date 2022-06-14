from minimax_tree.minimax_tree import MinimaxTree
from view import print_board
from model.board import Board
from contoller.command import starting_menu,choosing_player, print_menu, check_command_format, check_first_command_format


class GameController:
    turn = 0
    b = Board()

    def __init__(self):
        self.type_of_game = None
        self.minimax = None

    def start(self):
        self.type_of_game = starting_menu()
        if self.type_of_game == "Single player":
            self.Single_player()
        elif self.type_of_game == "Multiplayer":
            self.Multiplayer()

    def Single_player(self):
        self.turn = 0
        player = choosing_player()

        if player == "White":
            # first command input
            command = None
            while True:
                print_menu(self.turn)
                command = input()
                if check_first_command_format(command):
                    break

            command.strip()
            self.b.insert_piece(command, (0, 0), True, True)
            self.turn += 1
            print_board(self.b.board)
            self.minimax = MinimaxTree(self.b)

            # Game Loop
            while True:
                if self.turn % 2 == 0:
                    print_menu(self.turn)
                    command = input()
                    if command == "break":
                        self.good_bye()

                    if not check_command_format(command):
                        continue

                    commands = command.split(" ")

                    if self.turn == 6 and not "wQ1" in self.b.pieces and not commands[0][1] == "Q":
                        print("queen must entered in game before 5th turn")
                        continue

                    massage = self.b.read_command(commands[0], commands[1], commands[2])
                    if not massage == "ok":
                        print("\n\tError : " + massage)
                        continue

                    self.minimax.update_root(self.b)

                else:
                    self.ai_turn("black")

                if self.b.end_game():
                    return self.play_again()

                self.turn += 1
                print_board(self.b.board)

        else:
            # first command input
            command = None
            while True:
                print_menu(self.turn)
                command = input()
                if check_first_command_format(command):
                    break

            command.strip()
            self.b.insert_piece(command, (0, 0), True, True)
            self.turn += 1
            print_board(self.b.board)
            self.minimax = MinimaxTree(self.b)

            # Game Loop
            while True:
                if self.turn % 2 == 0:
                    print_menu(self.turn)
                    command = input()
                    if command == "break":
                        self.good_bye()

                    if not check_command_format(command):
                        continue

                    commands = command.split(" ")

                    if self.turn == 6 and not "wQ1" in self.b.pieces and not commands[0][1] == "Q":
                        print("queen must entered in game before 5th turn")
                        continue

                    massage = self.b.read_command(commands[0], commands[1], commands[2])
                    if not massage == "ok":
                        print("\n\tError : " + massage)
                        continue

                    self.minimax.update_root(self.b)

                else:
                    self.ai_turn("black")

                if self.b.end_game():
                    return self.play_again()

                self.turn += 1
                print_board(self.b.board)

    def Multiplayer(self):  # todo: check white-black turn
        self.turn = 0


        while True:
            print_menu(self.turn)
            command = input()
            if check_first_command_format(command):
                break

        command.strip()
        self.b.insert_piece(command, (0, 0), True, True)

        self.turn += 1

        print_board(self.b.board)

        # Game Loop
        while True:
            print_menu(self.turn)
            command = input()

            if command == "break":
                self.good_bye()

            if not check_command_format(command):
                continue

            commands = command.split(" ")

            if self.turn == 6 and not "wQ1" in self.b.pieces and not commands[0][1] == "Q":
                print("queen must entered in game before 5th turn")
                continue

            if self.turn == 7 and not "bQ1" in self.b.pieces and not commands[0][1] == "Q":
                print("queen must entered in game before 5th turn")
                continue

            massage = self.b.read_command(commands[0], commands[1], commands[2])
            if not massage == "ok":
                print("\n\tError : " + massage)
                continue
            if self.b.end_game():
                return self.play_again()

            self.turn += 1
            print_board(self.b.board)

    def ai_turn(self, color):
        print("\n------- HiveGame ------- ")
        print("$ turn : ", end='')
        print(color)
        print("$ AI : ")

        self.b = self.minimax.give_next_state()


    def play_again(self):
        print("\n\tDo you want play again ?")
        print("\t\t1) Yes")
        print("\t\t2) No")
        result = input("\t\t...")
        if result == "1":
            self.start()
        else:
            self.good_bye()


    @staticmethod
    def good_bye():
        print("Good Bye!")
        exit()
