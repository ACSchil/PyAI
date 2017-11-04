from copy import deepcopy
from collections import deque
from datetime import datetime
import sys


class Problem(object):
    """This is where the problem is defined. Initial state, goal state and
    other information that can be got from the problem"""
    # in Python 3.x, classes implicitly inherits object

    def __init__(self, initial, goal=None):
        """This is the constructor for the Problem class. It specifies
        the initial state, and possibly a goal state, if there is a unique
        goal.  You can add other arguments if the need arises"""
        self.metrics = Metrics()
        self.n = len(initial)
        self.size = pow(self.n, 2)
        self.goal = goal
        # Acquire sub-square dimensions
        if self.n == 4:
            self.subsquare_dimensions = (2, 2)
        elif self.n == 6:
            self.subsquare_dimensions = (2, 3)
        elif self.n == 9:
            self.subsquare_dimensions = (3, 3)
        else:
            print('Problem dimensions are not supported')
        # Determine number of pre-filled tiles
        self.completed = self.completed(initial)
        self.initial = SudokuState(initial, self.completed, (0, 0, 0))

    def completed(self, board):
        """Count the number of squares that have a number in them"""
        completed = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if board[i][j] != 0:
                    completed += 1
        return completed

    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a list, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        for i in range(state.last_action[0], self.n):
            if i == state.last_action[0]:
                for j in range(state.last_action[1], self.n):
                    if state.board[i][j] == 0:
                        return self.actionset(state.board, i, j)
            else:
                for j in range(0, self.n):
                    if state.board[i][j] == 0:
                        return self.actionset(state.board, i, j)

    def actionset(self, b, i, j):
        """Prune away any action that would violate Sudoku's rules"""
        actions = []
        violations = set()
        # Collect values in row
        for k in range(0, self.n):
            violations.add(b[i][k])
        # Collect values in column
        for k in range(0, self.n):
            violations.add(b[k][j])
        # Collect values in subs-quare
        n = -1
        m = -1
        if i < (1 * self.subsquare_dimensions[0]):
            n = 0
        elif i < (2 * self.subsquare_dimensions[0]):
            n = 1 * self.subsquare_dimensions[0]
        elif i < (3 * self.subsquare_dimensions[0]):
            n = 2 * self.subsquare_dimensions[0]
        if j < (1 * self.subsquare_dimensions[1]):
            m = 0
        elif j < (2 * self.subsquare_dimensions[1]):
            m = 1 * self.subsquare_dimensions[1]
        elif j < (3 * self.subsquare_dimensions[1]):
            m = 2 * self.subsquare_dimensions[1]
        for nn in range(n, n + self.subsquare_dimensions[0]):
            for mm in range(m, m + self.subsquare_dimensions[1]):
                violations.add(b[nn][mm])
        # Determine applicable actions
        for k in range(1, self.n + 1):
            if k not in violations:
                actions.append((i, j, k))
        return actions

    @staticmethod
    def result(state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        newboard = deepcopy(state.board)
        # Action is a touple (i, j, v) specifying the placement of v in cell i, j
        newboard[action[0]][action[1]] = action[2]
        newstate = SudokuState(newboard, state.completed + 1, action)
        return newstate

    def goal_test(self, state):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough.
        This must be written by students"""
        if state.completed != self.size:
            # We know the goal could only have been reached when we've filled n^2
            # tiles.
            return False
        else:
            # We don't need to check the tiles as this case will never be reached from an invalid state
            return True


class SudokuState:
    """A representation of the state of the sudoku board. Contains the board
    represented as a n x n matrix (a list of lists). Also contains a counter
    of the number of squares with a value and the action that was taken to get
    to this current state"""

    def __init__(self, board, completed, last_action):
        self.board = board
        self.completed = completed
        self.last_action = last_action


class Node:
    """A node in a search tree. Contains a pointer to the parent (the node
    that this is a successor of) and to the actual state for this node. Note
    that if a state is arrived at by two paths, then there are two nodes with
    the same state.  Also includes the action that got us to this state"""

    def __init__(self, state, parent=None, action=None):
        """Create a search tree Node, derived from a parent by an action.
        Update the node parameters based on constructor values"""
        self.state = state

    def expand(self, problem):
        # List the nodes reachable in one step from this node.
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action)


class Metrics:
    """Class for recording the number of nodes generated, nodes generated at
    each depth, and the time required to solve the puzzle"""

    def __init__(self):
        self.a = 0
        self.b = 0
        self.nodes = 0
        self.n = 0
        self.node = None

    def start(self):
        self.a = datetime.now()

    def stop(self):
        self.b = datetime.now()

    def delta(self):
        return self.b - self.a

    def incnode(self):
        self.nodes += 1

    def totalnodes(self):
        return self.nodes

    def updatemaxnodes(self, n):
        self.n = max(self.n, n)

    def nodesize(self, node):
        self.node = node

    def totalmemory(self):
        return self.nodes * sys.getsizeof(self.node)

    def maxmemory(self):
        return self.n * sys.getsizeof(self.node)

    def maxnodes(self):
        return self.n


def breadth_first_search(problem):
    """General BFS"""
    node = Node(problem.initial)
    if problem.goal_test(node.state):
        return node.state.board
    frontier = deque()
    frontier.append(node)
    ### metrics:
    try:
        problem.metrics.updatemaxnodes(len(frontier))
        problem.metrics.incnode()
    except NameError:
        pass
    ############
    while frontier:
        node = frontier.popleft()
        for child in node.expand(problem):
            if problem.goal_test(child.state):
                return child.state.board
            frontier.append(child)
            ### metrics:
            try:
                problem.metrics.incnode()
                problem.metrics.updatemaxnodes(len(frontier))
            except NameError:
                pass
            ############
    return None
