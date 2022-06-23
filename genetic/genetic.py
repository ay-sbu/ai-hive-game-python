import random
import numpy


from minimax_tree.minimax_tree import MinimaxTree
from model.board import Board
from view import print_board

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


def end_game(self):
    try:
        white_win = True
        x, y = self.pieces["bQ1"]
        arounds = self.around((x, y))
        for neighbour in arounds:
            x, y = neighbour
            if self.board[y][x] == []:
                white_win = False

        black_win = True
        x, y = self.pieces["wQ1"]
        arounds = self.around((x, y))
        for neighbour in arounds:
            x, y = neighbour
            if self.board[y][x] == []:
                black_win = False
        if white_win:
            if black_win:
                print("The game equalised")
                return True
            print("white")
            return True
        if black_win:
            print("black")
            return True
    except:
        pass
    return False


def mutation(generation_list):
    muted_list = []
    i = 0
    while i < len(generation_list):
        new_rand = random.randint(len(generation_list), len(generation_list) - 1)
        if new_rand not in muted_list:
            muted_list.append(new_rand)
            generation_list[new_rand][random.randint(0, max_of_parameters - 1)] = random.randint(1,
                                                                                                 max_of_parameters - 1)
            i += 1
    return generation_list


def cross_over(generation_list):
    kids = []
    for i in range(0, len(generation_list), 2):
        z = 0
        new_kid1 = []
        new_kid2 = []
        while z < max_of_parameters:
            if z < max_of_parameters // 2:
                new_kid1.append(generation_list[i][z])
                new_kid2.append(generation_list[i + 1][z])
            else:
                new_kid1.append(generation_list[i + 1][z])
                new_kid2.append(generation_list[i][z])
            z += 1
        kids.append(new_kid1)
        kids.append(new_kid2)
    return kids


def game(population):
    population_1 = population[:len(population) // 2]
    population_2 = population[len(population) // 2:]

    winner_population = []
    loser_population = []

    for i in range(len(population_1)):
        board = Board()
        board.insert_piece("wA1", (0, 0), True, True)
        minimax = MinimaxTree(board)

        minimax.first_heuristic = population_1[i]
        minimax.second_heuristic = population_2[i]

        while not board.end_game() and minimax.this_turn < 8:
            board.board = minimax.give_next_state()
            print_board(board.board.board)


        with open('log.txt', 'a') as f:
            line1 = "\n\ngame  "
            line2 = str(i)
            line3 = "\nAI1 parameters: "+str(winner_population)
            line4 = "\nAI2 parameters: "+str(loser_population)
            line5 = "\nwinner: "+str(winner_population)

            f.writelines([line1, line2, line3, line4, line5])

        f.close()
        if end_game(board.board) == "white":
            winner_population.append(population_2[i])
            loser_population.append(population_1[i])
        else:
            winner_population.append(population_1[i])
            loser_population.append(population_2[i])



    child = cross_over(winner_population[:len(winner_population) // 2])
    mutation_list_1 = mutation(winner_population[:len(winner_population) // 2])
    mutation_list_2 = mutation(loser_population[:len(loser_population) // 5])

    new_population = child + mutation_list_1 + mutation_list_2

    if numpy.std(new_population) > 0.8 or numpy.std(new_population) < 1.2:
        return new_population[0]
    else:
        game(new_population)



def genetic():
    population = initial_population()

    game(population)


if __name__ == '__main__':
    genetic()
