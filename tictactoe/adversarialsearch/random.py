import random


class Random:
    def __init__(self, name):
        self.name = name

    def get_move(self, board):
        actions = self.actions(board)
        decision = random.choice(actions)
        print('Random AI played ', self.name, ' at ', str(decision))
        return decision

    def actions(self, state):
        actions = []
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] == ' ':
                    actions.append((i, j))
        return actions
