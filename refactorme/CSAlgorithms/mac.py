from copy import copy
from collections import deque

def inference(csp, var, assignment):
    removed = {}
    removed[var.name] = set()
    a = assignment[var.name]
    # update csp with assignment
    for x in csp.X[var.name].domain:
        if x != a:
            csp.X[var.name].domain.remove(x)
            removed[var.name].add(x)
    if _ac3(csp, var, removed):
        return ('ok', removed)
    else:
        return ('failure', removed)

def _ac3(csp, var, removed):
    """Modified AC3 for use in MAC during backtracking"""
    queue = deque(var.neighbors)
    while len(queue) > 0:
        arc = queue.pop() # (Xi, Xj) <- Remove-First(queue)
        if arc.var1 not in removed.keys():
            removed[arc.var1] = set()
        if _revise(csp, arc, removed): # if Revise(csp, Xi, Xj) then
            if len(csp.X[arc.var1].domain) == 0: # if size of Di = 0 then return false
                return False
            for k in csp.X[arc.var1].neighbors: # for each Xk in Xi.Neighbors - Xj do add (Xk, Xi) to queue
                if k.var2 != arc.var2:
                    queue.appendleft(k)
    return True

def _revise(csp, arc, removed):
    """Returns true iff we revise the domain of Xi"""
    revised = False
    xd = copy(csp.X[arc.var1].domain)
    yd = copy(csp.X[arc.var2].domain)
    fn = arc.fn
    for x in xd:
        isConsistent = False
        for y in yd:
            if fn(x, y):
                isConsistent = True
                break
        if not isConsistent:
            csp.X[arc.var1].domain.remove(x)
            removed[arc.var1].add(x)
            csp.metrics.inc_pruned()
            revised = True
    return revised