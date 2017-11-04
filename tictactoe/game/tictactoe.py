from ast import literal_eval as make_tuple
from copy import copy, deepcopy


class TicTacToe:
    def __init__(self, n=3, mx=None, mo=None):
        self.n = n
        self.board = [[' ']*n for i in range(n)]
        self.actions = []
        for i in range(n):
            for j in range(n):
                self.actions.append((i,j))
        self.moves = 0

        self.playerx = _Player(n, 'x')
        self.playero = _Player(n, 'o')
        self.current = self.playerx

        self.mx = mx
        self.mo = mo

        self.last_move = None

    def get_board_state(self):
        board = []
        for i in range(self.n):
            board.append(tuple(self.board[i]))
        return tuple(board)

    def update_board(self, move):
        self.board[move[1][0]][move[1][1]] = move[0]
        if self.current.name == 'x':
            self.current = self.playero
        else:
            self.current = self.playerx
        self.last_move = move
        self.moves += 1
        self.actions.remove(copy(move[1]))

    def print_board(self):
        print('====='*self.n)
        for i in range(self.n):
            for j in range(self.n):
                print('| ' + self.board[i][j] + ' |', end='')
            print()
            print('====='*self.n)

    def run_hvh(self):
        while True:
            print()
            self.print_board()
            move = input('Player ' + self.current.name + ' place piece at: ')
            try:
                move = make_tuple(move)
            except:
                print('Invalid move! Try again. Format "(i,j)".')
            if len(move) != 2 or self.board[move[0]][move[1]] is not ' ':
                print('Invalid move! Try again.')
            else:
                self.current.update_moves(move)
                is_winner = self.current.is_winner()
                self.update_board((self.current.name, move))
                if is_winner:
                    break
            if self.moves == pow(self.n, 2):
                print()
                print('It\'s a tie! Game Over.')
                self.print_board()
                return
        print()
        print('Winner! Game Over.')
        self.print_board()

    def run_mvx(self):
        while True:
            print()
            self.print_board()
            if self.current.name == 'x' and self.mx is not None:
                move = self.mx.get_move(deepcopy(self.board))
            elif self.current.name == 'o' and self.mo is not None:
                move = self.mo.get_move(deepcopy(self.board))
            else:
                move = input('Player ' + self.current.name + ' place piece at: ')
                try:
                    move = make_tuple(move)
                except:
                    print('Invalid move! Try again. Format "(i,j)".')
                    continue
                if len(move) != 2 or self.board[move[0]][move[1]] is not ' ':
                    print('Invalid move! Try again.')
                    continue
            self.current.update_moves(move)
            is_winner = self.current.is_winner()
            self.update_board((self.current.name, move))
            if is_winner:
                break
            if self.moves == pow(self.n, 2):
                print()
                print('It\'s a tie! Game Over.')
                self.print_board()
                return
        print()
        print('Winner! Game Over.')
        self.print_board()


class _Player:
    def __init__(self, n, name):
        """Player instance. Maintains data on past and future moves. diag[0] corresponds to top
        left to bottom right diagonal, diag[1] from top right to the bottom left. Rows are ordered
        from top to bottom, and columns from left to right. If ever a row, column, or diagonal
        equals n, the player returns that it's the winner."""
        # to bottom left
        self.name = name
        self.n = n
        self.columns = [0]*n
        self.rows = [0]*n
        self.diags = [0]*2

    def is_winner(self):
        for i in range(self.n):
            if self.columns[i] == self.n:
                return True
            if self.rows[i] == self.n:
                return True
        if self.diags[0] == self.n or self.diags[1] == self.n:
            return True
        return False

    def update_moves(self, move):
        if move[0] == move[1]:
            self.diags[0] += 1
        if move[0] + move[1] == self.n - 1:
            self.diags[1] += 1
        self.rows[move[0]] += 1
        self.columns[move[1]] += 1
