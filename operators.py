BINARY_OPERATORS = ['/', '*', '<=', '>=', '==>', '<==>', '!=']
COMPLEX_OPERATORS = ['lim', 'int', 'sum', 'prod']
OTHER_OPERATORS = ['in', 'inc', 'nN', 'zZ', 'qQ', 'rR', 'cC', 'forall', 'exists', 'exists!']

def frac(numerator, denominator):
    return f'\\frac{{{numerator}}}{{{denominator}}}'

def times(a, b):
    return f'{a} \\cdot {b}'

def neq(a, b):
    return f'{a} \\neq {b}'

def geq(a, b):
    return f'{a} \\geqslant {b}'

def leq(a, b):
    return f'{a} \\leqslant {b}'