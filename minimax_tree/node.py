class Node:
    
    def __init__(self, board, children, parent, turn) -> None:
        self.board = board
        self.children = children
        self.parent = parent
        self.turn = turn
        self.score = None
        self.alpha = -1000
        self.beta = 10000
        
    