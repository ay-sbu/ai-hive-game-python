import copy
import string
from minimax_tree.node import Node


class MinimaxTree:
    
    last_depth = []
    depth_limit_checking = 7
    
    def __init__(self, root):
        print(f'root is {root}')
        self.root = root
        self.last_depth.append(root)
        self.first_tree_making()
    
    def first_tree_making(self):
        
        for _ in range(self.depth_limit_checking):
            self.make_and_update_last_depth()
    
    def make_and_update_last_depth(self):
        old_last_depth = copy.deepcopy(self.last_depth)
        self.last_depth = []
        for node in old_last_depth:
            nodes = possible_nodes(node)
            if nodes == []:
                continue
            node.children = nodes
            self.last_depth.append(node)
        return True
            
    def best_child(self):
        max = 0
        for node in self.last_depth:
            score = eval(node)
            if score > max:
                best_node = node
                max = score
                
        return best_node
            
            
    def ai_move(self) -> string:
        best = self.best_child()
        
        
            
def possible_nodes(board):
    pass

def eval(board):
    return len(board)
    
    