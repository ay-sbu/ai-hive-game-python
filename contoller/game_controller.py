def print_good_bye():
    print("Good Bye!")
    exit()


def print_menu():
    print("\n")
    print(" ------- HiveGame ------- ")
    print("input your command: ", end='')


class GameController:

    def start(self):
        print_menu()

        command = input()

        if command == "break":
            print_good_bye()

        # ToDo: handle bad format input here

        # Game Loop
        while True:
            print_menu()

            command = input()

            if command == "break":
                print_good_bye()

            # ToDo: handle bad format input here
