

class Pieces(object):

    def __init__(self, color, role, num):
        self.color = color  # can be 'b' or 'w'
        self.number = num  # can be [1, 2, 3]
        self.role = role  # one of ['A', 'B', 'L', 'Q', 'S']