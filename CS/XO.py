def new_board():
    new_board = [[0, 0, 0],
                 [0, 1, 0],
                 [0, 0, 0]]
    return new_board

def print_board(board):
    for row in range(3):
        print(row + 1, end=' ')
        for col in range(3):
            if board[row][col] == 0:
                print('|  ', end = ' ')
            elif board[row][col] == 1:
                print('| X', end = ' ')
            elif board[row][col] == 2:
                print('| O', end = ' ')
        print('|', '\n', ' -------------')
    print('  | 1 | 2 | 3 |')


board = new_board()
print(print_board(board))