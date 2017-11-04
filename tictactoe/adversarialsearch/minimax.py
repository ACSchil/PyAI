from copy import deepcopy
from operator import attrgetter
import random


class Minimax:
    def __init__(self, name):
        self.name = name

    def get_move(self, board):
        decision = self.minimax_decision(board)
        print('Minimax AI played ', self.name, ' at ', str(decision))
        return decision

    def minimax_decision(self, state):
        action_utilities = []
        actions = self.actions(state)
        for action in actions:
            new_state = self.result(state, action, self.name)
            utility = self.min_value(new_state, self.name)
            action_utilities.append(Action(action, utility))
        print('Possible Actions: ')
        for action in action_utilities:
            print(action)
        # max_action = max(action_utilities, key=attrgetter('utility'))
        max_action = self.decide(action_utilities)
        return max_action.action

    def max_value(self, state, old_player):
        player = None
        if old_player == 'x':
            player = 'o'
        elif old_player == 'o':
            player = 'x'
        terminal = self.terminal_test(state)
        if terminal == 'x' or terminal == 'o':
            return self.utility(terminal)
        elif terminal == True:
            return 0
        v = -2
        for action in self.actions(state):
            new_state = self.result(state, action, player)
            v = max(v, self.min_value(new_state, player))
        return v

    def min_value(self, state, old_player):
        player = None
        if old_player == 'x':
            player = 'o'
        elif old_player == 'o':
            player = 'x'
        terminal = self.terminal_test(state)
        if terminal == 'x' or terminal == 'o':
            return self.utility(terminal)
        elif terminal == True:
            return 0
        v = 2
        for action in self.actions(state):
            new_state = self.result(state, action, player)
            v = min(v, self.max_value(new_state, player))
        return v

    def actions(self, state):
        actions = []
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] == ' ':
                    actions.append((i, j))
        return actions

    def result(self, state, action, player):
        new_state = deepcopy(state)
        new_state[action[0]][action[1]] = player
        return new_state

    def terminal_test(self, state):
        # check if someone has won on a row
        for i in range(len(state)):
            row_winner = True
            row_marker = state[i][0]
            for j in range(len(state)):
                if state[i][j] != row_marker:
                    row_winner = False
                    break
            if row_winner == True:
                return row_marker
                # check if someone has won on a column
        for j in range(len(state)):
            column_winner = True
            column_marker = state[0][j]
            for i in range(len(state)):
                if state[i][j] != column_marker:
                    column_winner = False
                    break
            if column_winner == True:
                return column_marker
        # check if someone has won on a diagonal
        diag1_winner = True
        diag1_marker = state[0][0]
        for i in range(len(state)):
            if state[i][i] != diag1_marker:
                diag1_winner = False
                break
        if diag1_winner == True:
            return diag1_marker
        diag2_winner = True
        diag2_marker = state[0][len(state) - 1]
        i = 0
        j = len(state) - 1
        while i < len(state):
            check = state[i][j]
            if check != diag2_marker:
                diag2_winner = False
                break
            i += 1
            j -= 1
        if diag2_winner == True:
            return diag2_marker
        # check if board if full (and thus a tie, since no one won)
        board_full = True
        for i in range(len(state)):
            for j in range(len(state)):
                if state[i][j] == ' ':
                    board_full = False
                    break
            else:
                continue
            break
        if board_full == True:
            return True

    def utility(self, winner):
        if winner == self.name:
            return 1
        else:
            return -1

    def decide(self, action_utilities):
        actions = []
        for action in action_utilities:
            if action.utility == 1:
                actions.append(action)
        if len(actions) > 0:
            return random.choice(actions)
        for action in action_utilities:
            if action.utility == 0:
                actions.append(action)
        if len(actions) > 0:
            return random.choice(actions)
        for action in action_utilities:
            if action.utility == -1:
                actions.append(action)
        if len(actions) > 0:
            return random.choice(actions)


class Action:
    def __init__(self, action, utility=None):
        self.action = action
        self.utility = utility

    def __str__(self):
        return 'action: ' + str(self.action) + ' has utility: ' + str(self.utility)
