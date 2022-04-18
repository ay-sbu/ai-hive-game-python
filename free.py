from model import pieces
from model.board import Board


b = Board()


# b.insert_piece("bQ1", (0, 0))
# b.insert_piece("wQ1", (1, 4))
# b.insert_piece("bS2", (0, 5))
# b.add_row(True)
# b.add_column(True)
# b.add_column(False)
#
#
# print(b.piece_in_game("bQ1"))
b= [[[], ['wA1']], [['wA2'], []]]
b[0][1].remove('wA1')
print(b)

# print(b.pieces)
# for i in b.board:
#     print(i)
#
# pieces.can_move("bA1", (6, 5))



# Simple pygame program


# Import the pygame module
# import pygame
#
# # Import pygame.locals for easier access to key coordinates
# # Updated to conform to flake8 and black standards
# from pygame.locals import (
#     K_UP,
#     K_DOWN,
#     K_LEFT,
#     K_RIGHT,
#     K_ESCAPE,
#     KEYDOWN,
#     QUIT,
# )
#
# # Initialize pygame
# pygame.init()
#
#
# # Define a Player object by extending pygame.sprite.Sprite
# # The surface drawn on the screen is now an attribute of 'player'
# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super(Player, self).__init__()
#         self.surf = pygame.Surface((75, 25))
#         self.surf.fill((255, 255, 255))
#         self.rect = self.surf.get_rect()



# Import and initialize the pygame library
# board = [[[]]]
# board[0][1]=10
# print (board)
#
# newRow = []
# rowSize = len(board[0])
# for i in range(rowSize):
#     newRow.append([])
# if not before:
#     board.append(newRow)
# else:
#     y += 1
#     board.insert(0, newRow)

# board = [[[12, 14, 2, 6, 0], [2, 3, 4]], [[3, 6], [7, 10]], [0], [6]]
# print(board[0][1][0])
