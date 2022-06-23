import random
import numpy

# from model import pieces
# from model.board import Board
# from model.pieces import check_surrounding
# from view import print_board
# from minimax_tree.node import Node
# from model.pieces import around, check_continuity, initial_condition_for_move, ant_move, piece_naming, beetle_move, \
#     spider_move, queen_move
# import copy
#
#
# from view import print_board
# from random import random
# from minimax_tree.node import Node
# from model.pieces import around, check_continuity, initial_condition_for_move, ant_move, piece_naming, beetle_move, \
#     spider_move, queen_move
#
# #
# # b = Board()
# #
# #
# #
# #
# # b.board = [[[], ["bQ1"], []],
# #             [[], [], ["wA1"]],
# #             [[], [], ["wA1"]],
# #          [[], ["bS2"], []]]
# #
# # # print_board(b.board)
# # print(b.board)
#
#
#
#
#
#
#
# # print(b.piece_in_game("bQ1"))
# # b= [[[], ['wA1']], [['wA2'], []]]
# # b[0][1].remove('wA1')
# # print(b)
#
# # print(b.pieces)
# # for i in b.board:
# #     print(i)
# #
# # pieces.can_move("bA1", (6, 5))
#
#
#
# # Simple pygame program
#
#
# # Import the pygame module
# # import pygame
# #
# # # Import pygame.locals for easier access to key coordinates
# # # Updated to conform to flake8 and black standards
# # from pygame.locals import (
# #     K_UP,
# #     K_DOWN,
# #     K_LEFT,
# #     K_RIGHT,
# #     K_ESCAPE,
# #     KEYDOWN,
# #     QUIT,
# # )
# #
# # # Initialize pygame
# # pygame.init()
# #
# #
# # # Define a Player object by extending pygame.sprite.Sprite
# # # The surface drawn on the screen is now an attribute of 'player'
# # class Player(pygame.sprite.Sprite):
# #     def __init__(self):
# #         super(Player, self).__init__()
# #         self.surf = pygame.Surface((75, 25))
# #         self.surf.fill((255, 255, 255))
# #         self.rect = self.surf.get_rect()
#
#
#
# # Import and initialize the pygame library
# # board = [[[]]]
# # board[0][1]=10
# # print (board)
# #
# # newRow = []
# # rowSize = len(board[0])
# # for i in range(rowSize):
# #     newRow.append([])
# # if not before:
# #     board.append(newRow)
# # else:
# #     y += 1
# #     board.insert(0, newRow)
#
# # board = [[[12, 14, 2, 6, 0], [2, 3, 4]], [[3, 6], [7, 10]], [0], [6]]
# # print(board[0][1][0])
#
#
#
# def make_state_move(board, piece, position):
#     state = copy.deepcopy(board)
#     x, y = position
#
#     state.board[y][x] = board.board[y][x] + [piece]
#     state.pieces[piece] = (x, y)
#     state.resize_page(x,y)
#
#     return state
#
#
# def possible_movement(node, color):
#     possible_move = []
#
#     if ("bQ1" if color == "b" else "wQ1") not in node.board.pieces:
#         return possible_move
#     for piece in node.board.pieces:
#         if not piece[0] == color:
#             continue
#
#         piece_position = node.board.pieces[piece]
#         new_board = initial_condition_for_move(piece, node.board)
#         # new_board can be False or if continuity is True should be new board
#
#         if new_board is False:
#             continue
#
#         role = piece[1]
#
#         if role == "Q":
#             around = new_board.around(piece_position)
#             for position in around:
#                 x, y = position
#                 around_around = new_board.around((x, y))
#
#                 for position_position in around_around:
#                     xx, yy = position_position
#                     try:
#                         if not new_board.board[yy][xx] == []:
#                             if queen_move((x, y), piece_position, new_board, piece):
#                                 possible_move.append(make_state_move(new_board, piece, (x, y)))
#                     except:
#                         pass
#
#         elif role == "B":
#             around = new_board.around(piece_position)
#             for position in around:
#                 x, y = position
#                 around_around = new_board.around((x, y))
#
#                 for position_position in around_around:
#                     xx, yy = position_position
#                     try:
#                         if not new_board.board[yy][xx] == []:
#                             if beetle_move((x, y), piece_position, new_board, piece):
#                                 possible_move.append(make_state_move(new_board, piece, (x, y)))
#                     except:
#                         pass
#         elif role == "A":
#             for second_piece in new_board.pieces:
#                 around = new_board.around(new_board.pieces[second_piece])
#                 for position in around:
#                     x, y = position
#                     if not new_board.board[y][x] == []:
#                         continue
#                     if ant_move((x, y), node.board.pieces[piece], new_board, piece):
#                         possible_move.append(make_state_move(new_board, piece, (x, y)))
#         elif role == "S":
#             possible_positions = spider_move((0, 0), node.board.pieces[piece], new_board, piece, True)
#             for possible_position in possible_positions:
#                 possible_move.append(make_state_move(new_board, piece, possible_position))
#
#         # locust_possible_moves 6 direction(y/x): (no/l) (no/r) (l/l) (l/r) (r/l) (r/r)
#         # we move the locust by 6 whiles
#         else:
#             # no/l
#             x, y = piece_position
#             if new_board.board[y][x - 1] != []:
#                 x -= 1
#                 while True:
#                     x -= 1
#                     if new_board.board[y][x] == []:
#                         possible_position = (x, y)
#                         possible_move.append(make_state_move(new_board, piece, possible_position))
#                         break
#
#             # no/r
#             x, y = piece_position
#             if new_board.board[y][x + 1] != []:
#                 x += 1
#                 while True:
#                     x += 1
#                     if new_board.board[y][x] == []:
#                         possible_position = (x, y)
#                         possible_move.append(make_state_move(new_board, piece, possible_position))
#                         break
#
#             # l/l
#             x, y = piece_position
#             if new_board.board[y - 1][(x - 1) if y % 2 == 1 else x] != []:
#                 y -= 1
#                 if y % 2 == 1:
#                     x -= 1
#                 while True:
#                     y -= 1
#                     if y % 2 == 1:
#                         x -= 1
#                     if new_board.board[y][x] == []:
#                         possible_position = (x, y)
#                         possible_move.append(make_state_move(new_board, piece, possible_position))
#                         break
#
#             # l/r
#             x, y = piece_position
#             if new_board.board[y - 1][(x + 1) if y % 2 == 1 else x] != []:
#                 y -= 1
#                 if y % 2 == 1:
#                     x += 1
#                 while True:
#                     y -= 1
#                     if y % 2 == 1:
#                         x += 1
#                     if new_board.board[y][x] == []:
#                         possible_position = (x, y)
#                         possible_move.append(make_state_move(new_board, piece, possible_position))
#                         break
#
#             # r/l
#             x, y = piece_position
#             if new_board.board[y + 1][(x - 1) if y % 2 == 0 else x] != []:
#                 y += 1
#                 if y % 2 == 0:
#                     x -= 1
#                 while True:
#                     y += 1
#                     if y % 2 == 0:
#                         x -= 1
#                     if new_board.board[y][x] == []:
#                         possible_position = (x, y)
#                         possible_move.append(make_state_move(new_board, piece, possible_position))
#                         break
#
#             # r/r
#             x, y = piece_position
#             if new_board.board[y + 1][(x + 1) if y % 2 == 0 else x] != []:
#                 y += 1
#                 if y % 2 == 0:
#                     x += 1
#                 while True:
#                     y += 1
#                     if y % 2 == 0:
#                         x += 1
#                     if new_board.board[y][x] == []:
#                         possible_position = (x, y)
#                         possible_move.append(make_state_move(new_board, piece, possible_position))
#                         break
#
#     return possible_move
#
#
#
#
#
#
# b = Board()
#
# b.insert_piece("wA1", (0, 0), True, True)
#
# print_board(b.board)
# print()
#
# b.read_command("bQ1", "ne", "wA1")
# print_board(b.board)
# print()
#
#
# b.read_command("bB1", "e", "bQ1")
# print_board(b.board)
# print()
#
# b.read_command("bB2", "nw", "bQ1")
# print_board(b.board)
# print()
#
# b.read_command("wQ1", "sw", "wA1")
# print_board(b.board)
# print()
#
#
# node = Node(b,None, None, 5)
#
# print(possible_movement(node,"w"))
#
#
#
#
#
#









number_of_initial_population = 100
number_of_parameters = 3
max_of_parameters = 20


def initial_population():
    pop = []
    for i in range(number_of_initial_population):
        gene = []
        for j in range(number_of_parameters):
            gene.append(random.randint(1, max_of_parameters))
        # gene.append(0)
        pop.append(gene)
    return pop




def mutation(generation_list):
    muted_list = []
    i = 0
    while i < len(generation_list):
        new_rand = random.randint(0,len(generation_list)-1)
        if new_rand not in muted_list:
            muted_list.append(new_rand)

            generation_list[new_rand][random.randint(0, number_of_parameters - 1)] = random.randint(1,
                                                                                                 number_of_parameters - 1)
            i += 1
    return generation_list


def cross_over(generation_list):
    kids = []
    for i in range(0, len(generation_list)-1, 2):
        z = 0
        new_kid1 = []
        new_kid2 = []
        while z < number_of_parameters:
            if z < number_of_parameters // 2:
                new_kid1.append(generation_list[i][z])
                new_kid2.append(generation_list[i + 1][z])
            else:
                new_kid1.append(generation_list[i + 1][z])
                new_kid2.append(generation_list[i][z])
            z += 1
        kids.append(new_kid1)
        kids.append(new_kid2)
    return kids


def game(population,game_turn):
    population_1 = population[:len(population) // 2]
    population_2 = population[len(population) // 2:]

    winner_population = []
    loser_population = []

    for i in range(len(population_1)):

        if bool(random.getrandbits(1)):
            winner_population.append(population_2[i])
            loser_population.append(population_1[i])
            with open('log.txt', 'a') as f:
                line1 = "\n\ngame  "
                line2 = str(game_turn)
                line3 = "\nAI1 parameters: " + str(population_2[i])
                line4 = "\nAI2 parameters: " + str(population_1[i])
                line5 = "\nwinner: " + str(population_2[i])
                f.writelines([line1, line2, line3, line4, line5])
                f.close()

        else:
            winner_population.append(population_1[i])
            loser_population.append(population_2[i])
            with open('log.txt', 'a') as f:
                line1 = "\n\ngame  "
                line2 = str(i)
                line3 = "\nAI1 parameters: " + str(population_1[i])
                line4 = "\nAI2 parameters: " + str(population_2[i])
                line5 = "\nwinner: " + str(population_1[i])
                f.writelines([line1, line2, line3, line4, line5])
                f.close()

        game_turn += 1

    child = cross_over(winner_population[:len(winner_population) // 2])
    mutation_list_1 = mutation(winner_population[:len(winner_population) // 2])
    mutation_list_2 = mutation(loser_population[:len(loser_population) // 5])

    new_population = child + mutation_list_1 + mutation_list_2

    if numpy.std(new_population) > 0.8 or numpy.std(new_population) < 1.2:
        return new_population[0]
    else:
        game(new_population,game_turn)




def genetic():
    population = initial_population()

    game(population,0)


if __name__ == '__main__':
    genetic()
