import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    'abs': operator.abs,
    '^': operator.pow
}


def get_letter(n):
    if n == 0:
        return 'A'
    elif n == 1:
        return 'B'
    elif n == 2:
        return 'C'
    elif n == 3:
        return 'D'
    elif n == 4:
        return 'E'
    elif n == 5:
        return 'F'
