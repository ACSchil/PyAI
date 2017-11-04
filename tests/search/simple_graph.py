#######################
#    Problem Graph
#
#    b - f - g - h
#   /|\     / \ /
#  a | \   /   i
#   \|  \ /   /
#    c - d - e
#
#######################


class Problem:
    def __init__(self):
        self.initial = 'a'
        self.end = 'i'

    @staticmethod
    def actions(state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        if state == 'a':
            return ['b', 'c']
        elif state == 'b':
            return ['a', 'c', 'd', 'f']
        elif state == 'c':
            return ['a', 'b', 'd']
        elif state == 'd':
            return ['c', 'b', 'g', 'e']
        elif state == 'e':
            return ['d', 'i']
        elif state == 'f':
            return ['b', 'g']
        elif state == 'g':
            return ['f', 'd', 'i', 'h']
        elif state == 'h':
            return ['g', 'i']
        elif state == 'i':
            return ['g', 'h', 'e']

    @staticmethod
    def result(state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        return action

    @staticmethod
    def goal_test(state):
        if state == 'i':
            return True
        else:
            return False
