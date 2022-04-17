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
    
    

def check_first_command_format(command):
    commands = command.split()
    if len(commands) != 1 or not check_node_format(command):
            print("bad input format!")
            return False
    return True

def check_command_format(command):
    commands = command.split()
    if len(commands) != 3 or not check_node_format(commands[0]) or not check_place_format(commands[1]) or not check_node_format(commands[2]):
        print("bad input format!")
        return False
    
    
    return True



class GameController:
    turn = 0 # turn is 0(white) or 1(black)

    def start(self):
        
        # first command input
        print_menu()

        command = input()

        if command == "break":
            good_bye()
        
        if not check_first_command_format(command):
            good_bye()
            
        # TODO: Add to board
        
        self.change_turn()

        # Game Loop
        while True:
            print_menu()

            command = input()

            if command == "break":
                good_bye()
                
            
                
            if not check_command_format(command):
                continue
            
            
            print("After checking :) command sounds ok")
            
            
            self.change_turn()
            
    def change_turn(self):
        if self.turn == 1:
            self.turn = 0
        else:
            self.turn = 1
            
            
            
            
            
            
            
        
        
            
                
            
            

            
