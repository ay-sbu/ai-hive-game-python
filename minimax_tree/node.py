class Node:
    
    def __init__(self, board, children, parent, action) -> None:
        self.board = board
        self.children = children
        self.parent = parent
        self.action = action
        
    