from tictactoe.adversarialsearch.minimax import Minimax


def print_board(board):
    print('=====' * len(board))
    for i in range(len(board)):
        for j in range(len(board)):
            print('| ' + board[i][j] + ' |', end='')
        print()
        print('=====' * len(board))


# TODO automate

ai = Minimax('x')
print('Player x making move given state: ')
test1 = [['x', 'x', ' '], ['o', 'x', 'o'], [' ', 'o', ' ']]
print_board(test1)
action = ai.get_move(test1)
print('Player choose: ', str(action))

print()
print()

ai = Minimax('o')
print('Player o making move given state: ')
test1 = [['x', 'x', ' '], ['o', 'x', 'o'], [' ', 'o', ' ']]
print_board(test1)
action = ai.get_move(test1)
print('Player choose: ', str(action))

print()
print()

ai = Minimax('o')
print('Player o making move given state: ')
test1 = [['x', 'x', ' '], ['o', ' ', ' '], [' ', 'o', ' ']]
print_board(test1)
action = ai.get_move(test1)
print('Player choose: ', str(action))

print()
print()

ai = Minimax('x')
print('Player x making move given state: ')
test1 = [['x', 'x', ' '], ['o', ' ', ' '], [' ', 'o', ' ']]
print_board(test1)
action = ai.get_move(test1)
print('Player choose: ', str(action))

print()
print()

ai = Minimax('o')
print('Player o making move given state: ')
test1 = [['o', 'x', 'x'], [' ', 'o', ' '], ['x', 'o', 'x']]
print_board(test1)
action = ai.get_move(test1)
print('Player choose: ', str(action))

print()
print()

ai = Minimax('o')
print('Player o making move given state: ')
test1 = [['x', ' ', 'x'], ['o', ' ', ' '], ['x', 'o', ' ']]
print_board(test1)
action = ai.get_move(test1)
print('Player choose: ', str(action))
