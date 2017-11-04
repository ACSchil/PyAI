from datetime import datetime
import sys

class Metrics:
    """Class for recording the number of nodes generated,
    and the time required to solve the puzzle. Instantiate
    while instantiated a search problem."""

    def __init__(self):
        self.a = 0  # start time
        self.b = 0  # end time
        self.assignments = 0  # number of times we make an assignment
        self.pruned = 0  # number of values pruned during inference
        self.times_backtracked = 0  # number of times backtracking search sees a failure

    def start(self):
        if self.a != 0:
            return
        self.a = datetime.now()

    def stop(self):
        self.b = datetime.now()

    def inc_assignments(self):
        self.assignments += 1

    def inc_pruned(self):
        self.pruned += 1

    def inc_backtracked(self):
        self.times_backtracked += 1

    def get_metrics(self):
        """Print of search performance metrics"""
        print(' === problem metrics ===')
        if self.b == 0:
           self.stop()
        print('Problem solved in (s): ', self.b - self.a)
        print('Total assignments: ', self.assignments)
        print('Assignments Pruned: ', self.pruned)
        print('Number of time backtracked: ', self.times_backtracked)
        sys.stdout.flush()
