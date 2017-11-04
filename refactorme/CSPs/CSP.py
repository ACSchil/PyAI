from collections import deque
from refactorme.Helpers.metrics import Metrics


class CSP:
    def __init__(self):
        self.domain = []
        self.X = {}  # name mapped to Var, which has name, domain, neighbors
        self.C = deque()  # queue of Constraints
        self.metrics = Metrics()

    def get_arcs(self):
        return self.C


class Var:
    def __init__(self, n, d):
        self.name = n
        self.domain = d
        self.neighbors = []

    def add_neighbor(self, neighbor):
        """Neighbors are of the form (Vk, Vi), where Vk is a neighboring is a
        neighboring node (has a constraint) with Vi the node we are currently \
        considering"""
        self.neighbors.append(neighbor)


class Constraint:
    """n-ary constraint such that n < 6"""
    def __init__(self, num_vars, fn, var1, op1=None, var2=None, op2=None,
                 var3=None, op3=None, var4=None, op4=None, var5=None, val=None):
        self.fn = fn
        self.num_vars = num_vars
        self.var1 = var1
        self.op1 = op1
        self.var2 = var2
        self.op2 = op2
        self.var3 = var3
        self.op3 = op3
        self.var4 = var4
        self.op4 = op4
        self.var5 = var5
        self.val = val

    def print_constraint(self):
        print(self.var1, end='')
        if self.op1 is not None:
            print(self.op1, self.var2, end='')
        if self.op2 is not None:
            print(self.op2, self.var3, end='')
        if self.op3 is not None:
            print(self.op3, self.var4, end='')
        if self.op4 is not None:
            print(self.op4, self.var5, end='')
        if self.val is not None:
            print('=', self.val, end='')
        print()
