from copy import copy

def ac3(csp):
    """Returns false if an inconsistency is found and true otherwise"""
    queue = csp.get_arcs()
    while len(queue) > 0:
        arc = queue.pop() # (Xi, Xj) <- Remove-First(queue)
        if revise(csp, arc): # if Revise(csp, Xi, Xj) then
            if len(csp.X[arc.var1].domain) == 0: # if size of Di = 0 then return false
                return False
            for k in csp.X[arc.var1].neighbors: # for each Xk in Xi.Neighbors - Xj do add (Xk, Xi) to queue
                if k.var2 != arc.var2:
                    queue.appendleft(k)
    return True

def revise(csp, arc):
    """Returns true iff we revise the domain of Xi"""
    revised = False
    xd = copy(csp.X[arc.var1].domain)
    yd = copy(csp.X[arc.var2].domain)
    fn = arc.fn
    for x in xd:
        isConsistent = False
        for y in yd:
            #print( x, arc.op1, y, arc.fn(x,y))
            #print( y, arc.op1, x, arc.fn(y,x), ' flipped')
            if fn(x, y):
                isConsistent = True
                break
        if not isConsistent:
            csp.X[arc.var1].domain.remove(x)
            revised = True
    return revised