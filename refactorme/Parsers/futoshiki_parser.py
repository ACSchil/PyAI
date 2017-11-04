import re

from refactorme.Helpers.helpers import ops
from refactorme.CSPs.CSP import Constraint


def readFutoshiki(puzzle):
    """Returns a list of constraints. Constraints can be one of two types:
    ('u', var, val, fn) or ('b', var1, var2, fn), where 'u' denotes unary,
    'b' denotes binary."""
    constraints = []
    # read in the file with constraints for KenKen puzzles (1 line per puzzle)
    lines = open(puzzle).readlines()
    testLine = 0 # test this line in file
    l = lines[testLine]
    #remove white space
    l = re.sub('[ ]','',l)
    #print('l ',l)

    # size of puzzle is first number on the line
    n = eval(re.findall('^\d+',l)[0])
    l = re.sub('^\d+','',l)
    #print('size ',n)

    # find all "x Op y"
    cs=re.findall('\w+\W+\w+',l)
    #print('c ',cs)

    # for each, separate apart the variables, operator, and values
    for c in cs:
        # these are x < y OR x > y
        if re.findall('\w+\d+<\w+\d+',c) or re.findall('\w+\d+>\w+\d+',c):
            lvar = re.findall('^\w+\d+',c)[0]
            rvar = re.findall('\w+\d+$',c)[0]
            op = re.findall('\W',c)[0]
            constraint = Constraint(2, fn=lambda x,y: ops[op](x,y), var1=lvar, op1=op, var2=rvar)
            #constraint.print_constraint()
            constraints.append(constraint)
            if op == '<':
                constraint = Constraint(2, fn=lambda x,y: ops['>'](x,y), var1=rvar, op1='>', var2=lvar)
                #constraint.print_constraint()
                constraints.append(constraint)
            elif op == '>':
                constraint = Constraint(2, fn=lambda x,y: ops['<'](x,y), var1=rvar, op1='<', var2=lvar)
                #constraint.print_constraint()
                constraints.append(constraint)
        else:
            # find x = value
            if re.findall('\w+\d+=\d+',c):
                var = re.findall('^\w+\d+',c)[0]
                value = re.findall('\d+$',c)[0]
            # find value = x
            elif re.findall('\d+=\w+\d+',c):
                var = re.findall('\w+\d+$',c)[0]
                value = re.findall('^\d+$',c)[0]
            # convert equalities to lambda fn
            # test results with a print
            #print('var,val,fn(1) ',var,'==',value,f(1))
            if (var is not None and value is not None):
                constraint = Constraint(1, fn=lambda x: x == eval(value), var1=var, val=int(value))
                constraints.append(constraint)
            else:
                print('err: no var/value pair for unary constraint')
    return (n, constraints)