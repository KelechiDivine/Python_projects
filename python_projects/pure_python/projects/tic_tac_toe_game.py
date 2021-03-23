# Tic Tac Toe
the_board = {'top left': ' ', 'top middle': ' ', 'top right': ' ',
             'middle left': ' ', 'middle middle': ' ', 'middle right': ' ',
             'low left': ' ', 'low middle': ' ', 'low right': ' '}


def print_board(board):
    print(board['top left'] + '|' + board['top middle'] + '|' + board['top right'])
    print('-+-+-')
    print(board['middle left'] + '|' + board['middle middle'] + '|' + board['middle right'])
    print('-+-+-')
    print(board['low left'] + '|' + board['low middle'] + '|' + board['low right'])
turn = 'x'


for i in range(9):
    print_board(the_board)
    print("Turn for " + turn + '. Move on which space? ')
    move = input("Please Give an input! ")
    the_board[move] = turn
    if turn == 'x':
        turn = 'o'
    else:
        turn = 'x'

print_board(the_board)
