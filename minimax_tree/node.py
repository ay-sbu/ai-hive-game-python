class Node:
    
    def __init__(self, board, children, parent, turn) -> None:
        self.board = board
        self.children = children
        self.parent = parent
        self.turn = turn
        
    