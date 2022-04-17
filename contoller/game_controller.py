import string


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
    if string_node[0] != 'w' or string_node[0] != 'b':
        return False
    
    if string_node[1] != 'B' and \
        string_node[1] != 'Q' and \
        string_node[1] != 'L' and \
        string_node[1] != 'S' and \
        string_node[1] != 'A':
        return False


def check_first_command_format(command):
    commands = command.split()
    if len(commands) != 1 and check_node_format(command):
            print("bad input format!")
            return False
    return True

def check_command_format(command):
    commands = command.split()
    if len(commands) != 3 and check_node_format(commands[0]) and check_place_format(command[1]) and check_node_format(commands[2]):
        print("bad input format!")
        return False
    
    
    return True

def change_turn():
    if GameController.turn == 1:
        GameController.turn = 0
    else:
        GameController.turn = 1

class GameController:
    turn = 0 # turn is 0(white) or 1(black)

    def start(self):
        
        # first command input
        print_menu()

        command = input()

        if command == "break":
            good_bye()

        is_correct_format = check_first_command_format(command)
        
        if not is_correct_format:
            good_bye()
            
        # TODO: Add to board
        
        change_turn()

        # Game Loop
        while True:
            print_menu()

            command = input()

            if command == "break":
                good_bye()
                
            if not is_correct_format:
                continue
            
            
            
            
            
            change_turn()
            
            
            
            
            
            
            
        
        
            
                
            
            

            
