from datetime import datetime
import sys


class Metrics:
    """Class for recording the number of nodes generated,
    and the time required to solve the puzzle. Instantiate
    while instantiated a search problem."""

    def __init__(self):
        self.a = 0
        self.b = 0
        self.nodes = 0
        self.nodesize = 0
        self.frontier = 0
        self.explored = 0
        self.depth = 0
        self.solution_steps = 0

    def start(self):
        if self.a != 0:
            return
        self.a = datetime.now()

    def stop(self):
        self.b = datetime.now()

    def node_size(self, node):
        """Determines size in bytes of the node for the problem.
        Used to estimate memory usage"""
        self.nodesize = sys.getsizeof(node)

    def inc_node(self):
        """Used to count the number of generated nodes; note, this
        is different than the number of nodes explored"""
        self.nodes += 1

    def update_max_depth(self, d):
        """For recursive problem, this tracks the maximum depth
        reached"""
        self.depth = max(self.depth, d)

    def update_max_frontier(self, f):
        self.frontier = max(self.frontier, f)

    def update_max_explored(self, e):
        self.explored = max(self.explored, e)

    def update_solution_steps(self, s):
        """Count the number of nodes along the path from the initial
        state to the goal state of the solution returned from a
        search"""
        self.solution_steps = s

    def get_metrics(self):
        try:
            """Print of search performance metrics"""
            print(' === problem metrics ===')
            print('Problem finished in (s): ', self.b - self.a)
            print('Nodes generated: ', self.nodes)
            print('Max depth: ', self.depth)
            print('Max nodes explored: ', self.explored)
            print('Max nodes on frontier: ', self.frontier)
            print('Nodes along solution path: ', self.solution_steps)
            print('Node size in bytes: ', self.nodesize)
        except Exception as e:
            print('Encountered an exception while reporting metrics. Exiting. Cause: ', e)
        print()
        sys.stdout.flush()
