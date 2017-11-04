from tictactoe.game.tictactoe import TicTacToe
from tictactoe.adversarialsearch.minimax import Minimax


def main():
    ai = Minimax('o')
    t = TicTacToe(mo=ai)
    t.run_mvx()


if __name__ == '__main__':
    main()
