
def starting_menu():
    print("\n\n\t\t\t\t\t\tWelcome to Hive Game :) ..... Let's go ")
    print("\n\nPlease chose type of your game :")
    print("\t1) Single player")
    print("\t2) Multiplayer")
    while True:
        type_of_game = input("\n\t...")
        if type_of_game == "1":
            return "Single player"
        elif type_of_game == "2":
            return "Multiplayer"
        print("\tOnly choose from options :(")


def choosing_player():
    print("\n\nChoose your color :")
    print("\t1) White")
    print("\t2) Black")
    while True:
        player = input("\n\t...")
        if player == "1":
            return "White"
        elif player == "2":
            return "Black"
        print("\tOnly choose from options :(")


def print_menu(turn):
    print("\n")
    print("------- HiveGame ------- ")
    print("$ turn : ", end='')
    if turn % 2 == 0:
        print("white")
    else:
        print("black")

    print("$ input your command > ", end='')


def check_command_format(command):
    commands = command.split()
    if len(commands) != 3 or not check_node_format(commands[0]) or \
            not check_place_format(commands[1]) or not check_node_format(commands[2]) :
        print("bad input format!")
        return False

    return True


def check_first_command_format(command):
    commands = command.split()
    if len(commands) != 1 or not check_node_format(command) :
        print("bad input format!")
        return False
    return True



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
