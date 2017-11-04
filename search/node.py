class Node:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action

    def expand(self, problem):
        """Return a list of nodes reachable by applying all applicable actions to this node."""
        return [self.child_node(problem, action)
                for action in problem.actions(self.state)]

    def child_node(self, problem, action):
        """Generate a child Node from this Node by applying the specified action parameter."""
        next_node = problem.result(self.state, action)
        return Node(next_node, self, action)
