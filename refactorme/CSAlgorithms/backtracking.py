from refactorme.CSAlgorithms import fc, mac
from copy import copy


def backtracking_search(csp):
    return _backtrack({}, csp, _select_unassigned_var, _order_domain_values, _inference)


def fc_backtracking_search(csp):
    return _backtrack({}, csp, _select_unassigned_var, _order_domain_values, fc.inference)


def mac_backtracking_search(csp):
    return _backtrack({}, csp, _select_unassigned_var, _order_domain_values, mac.inference)


def _backtrack(assignment,
               csp,
               select_unassigned_var,
               order_domain_values,
               inference):
    if len(assignment) == csp.size:
        return assignment
    var = select_unassigned_var(csp, assignment)
    for value in order_domain_values(var, assignment, csp):
        csp.metrics.inc_assignments()
        inferences = None
        if _is_consistent(var, value, assignment):
            assignment[var.name] = value
            inferences = inference(csp, var, assignment)
            if inferences[0] != 'failure':
                result = _backtrack(assignment,
                                    csp,
                                    select_unassigned_var,
                                    order_domain_values,
                                    inference)
                if result != 'failure':
                    return result
        csp.metrics.inc_backtracked()
        assignment.pop(var.name, None)
        _restore(assignment, inferences, csp)
    return 'failure'


def _select_unassigned_var(csp, assignment):
    for x in csp.X.keys():
        if x not in assignment.keys():
            return csp.X[x]


def _is_consistent(var, value, assignment):
    is_consistent = True
    for k in var.neighbors:
        if k.var1 not in assignment.keys():
            continue
        elif not k.fn(assignment[k.var1], value):
            is_consistent = False
            break
    return is_consistent


def _order_domain_values(var, assignment, csp):
    return copy(var.domain)


def _inference(csp, var, assignment):
    return ('ok', None)


def _restore(assignment, inferences, csp):
    if inferences is None or inferences[1] is None:
        return
    for k in inferences[1].keys():
        # restore each value
        for v in inferences[1][k]:
            csp.X[k].domain.append(v)
