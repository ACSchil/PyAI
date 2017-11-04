from copy import copy


def inference(csp, var, assignment):
    removed = {}
    removed[var.name] = set()
    a = assignment[var.name]
    neighbors = var.neighbors
    # update csp with assignment
    for x in csp.X[var.name].domain:
        if x != a:
            csp.X[var.name].domain.remove(x)
            removed[var.name].add(x)
    # initialize all inferences on neighbors to the empty set, i.e.
    # initially we remove no values from the domains of the var's
    # neighbors
    for n in neighbors:
        if n.var1 not in removed.keys():
            removed[n.var1] = set()
    # establish arc consistency given the assignment for each neighbor
    # of the var
    for n in neighbors:
        if _fc(csp, n, removed, assignment[var.name]) == 'failure':
            return ('failure', removed)
    return ('ok', removed)


def _fc(csp, arc, removed, val):
    xd = copy(csp.X[arc.var1].domain)
    fn = arc.fn
    # for each value that is inconsistent with the new assignment,
    # add it to the inferences to have it be removed
    for x in xd:
        if not fn(x, val):
            # remove inconsistent value from the domain
            csp.X[arc.var1].domain.remove(x)
            # book-keep removal
            removed[arc.var1].add(x)
            csp.metrics.inc_pruned()
    # if the domain was reduced to zero, this is an invalid assignment
    if len(csp.X[arc.var1].domain) == 0:
        return 'failure'
    else:
        return 'ok'
