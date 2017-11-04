from collections import deque
from copy import deepcopy
from random import shuffle

from towersofhanoi.metrics import Metrics


class TowersOfHanoi:
    def __init__(self, discs, pegs=3):
        """Constructor builds a Towers of Hanoit problem with a given
        number of discs and pegs. The default number of pegs is 3."""
        self.metrics = Metrics()
        self.discs = discs
        self.pegs = pegs
        # problem is a list of deques
        self.towers = []
        # build towers
        for t in range(0, pegs):
            self.towers.append(deque(maxlen=discs))
        # place all discs on first tower
        for d in range(discs, 0, -1):
            self.towers[0].append(d)
        self.initial = self.towers
        self.end = list(reversed(self.towers))
        # print("initialized state to: ")
        # self.print_state(self.initial)

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. actions is a list of tuple specifying the (from, to)"""
        actions = []
        # for each tower, peek at the disc (denoted d) on top
        for from_peg in range(0, self.pegs):
            # todo: peek
            try:
                from_peg_size = state[from_peg].pop()
                state[from_peg].append(from_peg_size)
            except IndexError:
                continue
            # for all other towers, peek at the disc (denoted d') on top
            for to_peg in range(0, self.pegs):
                to_peg_size = -1
                if to_peg != from_peg:
                    try:
                        to_peg_size = state[to_peg].pop()
                        state[to_peg].append(to_peg_size)
                    except IndexError:
                        to_peg_size = self.discs + 1
                # if d' is larger than d, placing d onto the peg with d' is an applicable action
                if from_peg_size < to_peg_size:
                    actions.append((from_peg, to_peg))
        shuffle(actions)
        return actions
        # return actions

    @staticmethod
    def result(state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        # copy the state
        child_state = deepcopy(state)
        # action[0] holds the peg from which to pop the top disc
        disc = child_state[action[0]].pop()
        # action[1] holds the peg to append the popped disc to
        child_state[action[1]].append(disc)
        return child_state

    def goal_test(self, state):
        """Return True if the state is a goal."""
        # if all discs are on the final peg we've arrived at the goal state
        if len(state[self.pegs - 1]) == self.discs:
            # print("reached goal state:")
            # self.print_state(state)
            return True
        else:
            return False

    def print_state(self, state):
        """Prints a state"""
        for p in range(0, self.pegs):
            print("|", end='')
            for d in range(0, len(state[p])):
                print(state[p][d], end=" ")
            print()


class CyclicHanoi(TowersOfHanoi):
    """A variation on the classic Towers of hanoi where discs can only
    be moved in a counterclockwise direction. E.g. if we have towers
    1, 2, 3 a disc from tower 1 can only be moved to tower 2. A disc from
    tower 2 can only be moved to tower 3; a disc from tower 3 can only
    be moved to tower 1."""

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. actions is a list of tuple specifying the (from, to)"""
        actions = []
        # for each tower, peek at the disc (denoted d) on top
        for from_peg in range(0, self.pegs):
            # todo: peek
            try:
                from_peg_size = state[from_peg].pop()
                state[from_peg].append(from_peg_size)
            except IndexError:
                continue
            # for all other towers, peek at the disc (denoted d') on top
            to_peg = from_peg + 1
            if to_peg > self.pegs - 1:
                to_peg = 0
            try:
                to_peg_size = state[to_peg].pop()
                state[to_peg].append(to_peg_size)
            except IndexError:
                to_peg_size = self.discs + 1
            # if d' is larger than d, placing d onto the peg with d' is an applicable action
            if from_peg_size < to_peg_size:
                actions.append((from_peg, to_peg))
        return actions


def immutable_hanoi(state):
    """Takes the state as a list of deques and returns an equivalent, but immutable
    tuple of tuples; used for hashing states"""
    towers = []
    for t in range(0, len(state)):
        towers.append(tuple(state[t]))
    return tuple(towers)
