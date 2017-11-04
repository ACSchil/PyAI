import re
from copy import copy
from refactorme.Helpers.helpers import ops
from refactorme.CSPs.CSP import Constraint

def readCrossMath(file):
    constraints = []
    # I was assuming operators applied in order as listed on puzzle, but
    # probably supposed to follow op precedence. If so, this isn't quite right.

    # read in the file with constraints for KenKen puzzles (1 line per puzzle)
    lines = open(file).readlines()
    testLine = 0 # test this line in file
    l = lines[testLine]
    #remove white space
    l=re.sub('[ ]','',l)
    print('l ',l)

    # split into the different constraints
    cs=re.split(',',l)
    #print('cs ',cs)

    # for each constraint, extract vars and create lambda
    for c in cs:
        # extract what the equation equates to
        answer = re.findall('=\d+',c)
        answer = re.sub('=','',answer[0])
        c = re.sub('=\d+','',c)

        groupRight = False
        # check for parantheses for precedence
        if re.search('\)',c):
            if ( re.search('\)',c).start() == len(c)-2 ):
                groupRight = True
                c = re.sub('\(','',c)
                c = re.sub('\)','',c)

        # extract the 2 operators and the 3 vars, create the function
        op2 = re.findall('\W',c)
        var3 = re.findall('\w+\d+',c)

        #print('c ',c)
        if groupRight:
            fn = lambda x,y,z : ops[op2[0]](x,ops[op2[1]](y,z)) == eval(answer)
            constraint = Constraint(3, fn=lambda x,y,z : ops[op2[0]](x,ops[op2[1]](y,z)) == eval(answer),
                                    var1=var3[0], var2=var3[1], var3=var3[2],
                                    op1=op2[0], op2=op2[1], val=answer)
            #constraint.print_constraint()
            constraints.append(constraint)
        else:
            fn = lambda x,y,z : ops[op2[1]](ops[op2[0]](x,y),z) == eval(answer)
            constraint = Constraint(3, lambda x,y,z : ops[op2[1]](ops[op2[0]](x,y),z) == eval(answer),
                                    var1=var3[0], var2=var3[1], var3=var3[2],
                                    op1=op2[0], op2=op2[1], val=answer)
            #constraint.print_constraint()
            constraints.append(constraint)

        # test the results with a print
        #print('op var answer fn(16,16,4)',op2,' ',var3,' ',answer,' ',fn(16,16,4))
    return (3, constraints)

if __name__ == "__main__":
    #readKenKen()
    #readCrypt()
    #readFutoshiki()
    readCrossMath()