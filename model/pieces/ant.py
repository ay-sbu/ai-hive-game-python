from model.pieces.pices import Pieces


class Beetle(Pieces):
    def __init__(self, color, kind, number):
        super().__init__(color, number)

    def permitted_movements(self, location):



