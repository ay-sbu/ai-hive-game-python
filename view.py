def print_board(board):
    for i in range(len(board[0])):
        print(" / \\", end='')

    print()

    for i in range(len(board)):
        row = board[i]

        if i % 2 == 1:
            print(" " * 2, end="")

        for col in row:
            print("|", end='')
            if len(col) == 0:
                print(" " * 3, end='')
            else:
                print(col[-1], end='')

        print("|")

        if i % 2 == 1:
            print(" /", end='')

        for col in row:
            print(" \\ /", end='')

        if i % 2 == 0 and len(board) != i + 1:
            print(" \\", end="")

        print()
