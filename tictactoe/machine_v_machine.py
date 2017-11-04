from tictactoe.game.tictactoe import TicTacToe
from tictactoe.adversarialsearch.minimax import Minimax
from tictactoe.adversarialsearch.random import Random


def main():
    print()
    print('===================')
    print(' Minimax v Minimax ')
    print('===================')
    print()
    aix = Minimax('x')
    aio = Minimax('o')
    t = TicTacToe(mx=aix, mo=aio)
    t.run_mvx()

    print()
    print('==================')
    print(' Minimax v Random ')
    print('==================')
    print()
    aix = Minimax('x')
    aio = Random('o')
    t = TicTacToe(mx=aix, mo=aio)
    t.run_mvx()

    print()
    print('==================')
    print(' Random v Minimax ')
    print('==================')
    print()
    aio = Minimax('o')
    aix = Random('x')
    t = TicTacToe(mx=aix, mo=aio)
    t.run_mvx()


if __name__ == '__main__':
    main()
