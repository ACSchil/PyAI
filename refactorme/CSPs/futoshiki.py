from copy import copy

from refactorme.Helpers.helpers import ops, get_letter
from refactorme.CSPs.CSP import CSP, Var, Constraint

class FutoshikiCSP(CSP):
    """All CSPs must contain a set/dictionary of variables X (which contains
    a name, domain, and neighborhood), and function get_arcs() that returns
    a deque of constraints"""
    def __init__(self, n, constraints):
        super(FutoshikiCSP, self).__init__()
        self.size = pow(n, 2)
        # build up D
        for i in range (1, n+1):
            self.domain.append(i)
        # build up X
        for a in range(0, n):
            for b in range(1, n+1):
                var = get_letter(a) + str(b)
                self.X[var] = Var(var, copy(self.domain))
        for c in constraints:
            # unary constraints (satisfy immediately)
            if c.num_vars == 1:
                self.X[c.var1].domain.clear()
                self.X[c.var1].domain.append(c.val)
            # binary constraints
            elif c.num_vars == 2:
                #c.print_constraint()
                self.C.append(c)
                if c.op1 == '>':
                    neighbor = Constraint(2, fn=lambda x,y: ops['<'](x,y), var1=c.var2, op1='<<', var2=c.var1)
                    self.X[c.var1].add_neighbor(neighbor)
                elif c.op1 == '<':
                    neighbor = Constraint(2, fn=lambda x,y: ops['>'](x,y), var1=c.var2, op1='>>', var2=c.var1)
                    self.X[c.var1].add_neighbor(neighbor)
        # add alldiff rules to binary constraints
        fn = lambda x, y: x != y
        for a in range(0, n):
            for b in range(1, n+1):
                v1 = get_letter(a) + str(b)
                for c in range(1, n+1):
                    v2 = get_letter(a) + str(c)
                    if v1 != v2:
                        constraint = Constraint(2, fn, v1, op1='!=', var2=v2)
                        self.C.append(constraint)
                        neighbor = Constraint(2, fn, v2, op1='!=', var2=v1)
                        self.X[v1].add_neighbor(neighbor)
        fn = lambda x, y: x != y
        for b in range(1, n+1):
            for a in range(0, n):
                v1 = get_letter(a) + str(b)
                for c in range(0, n):
                    v2 = get_letter(c) + str(b)
                    if v1 != v2:
                        constraint = Constraint(2, fn, v1, op1='!=', var2=v2)
                        self.C.append(constraint)
                        neighbor = Constraint(2, fn, v2, op1='!=', var2=v1)
                        self.X[v1].add_neighbor(neighbor)

