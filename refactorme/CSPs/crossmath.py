from copy import copy
from refactorme.Helpers.helpers import ops, get_letter
from refactorme.CSPs.CSP import CSP, Var, Constraint
from refactorme.Helpers.helpers import ops
from refactorme.Parsers import crossmath_parser

class CrossmathCSP(CSP):
    """All CSPs must contain a set/dictionary of variables X (which contains
    a name, domain, and neighborhood), and function get_arcs() that returns
    a deque of constraints"""
    def __init__(self, n, constraints):
        super(CrossmathCSP, self).__init__()
        self.size = pow(n, 2)
        # build up D
        for i in range (1, self.size+1):
            self.domain.append(i)
        # build up X
        for a in range(0, n):
            for b in range(1, n+1):
                var = get_letter(a) + str(b)
                self.X[var] = Var(var, copy(self.domain))
        for c in constraints:
            self.C.append(c)
        # add alldiff rules
        fn = lambda x, y: x != y
        for a in range(0, n):
            for b in range(1, n+1):
                v1 = get_letter(a) + str(b)
                for c in range(0, n):
                    for d in range(1, n+1):
                        v2 = get_letter(c) + str(d)
                        if v1 != v2:
                            constraint = Constraint(2, fn, v1, op1='!=', var2=v2)
                            self.C.append(constraint)
                            neighbor = Constraint(2, fn, v2, op1='!=', var2=v1)
                            self.X[v1].add_neighbor(neighbor)

if __name__ == "__main__":
    c = crossmath_parser.readCrossMath()
    csp = CrossmathCSP(c[0], c[1])
    for c in csp.C:
        c.print_constraint()