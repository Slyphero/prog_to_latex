BINARY_OPERATORS = ['/', 'lim', 'int']
TERNARY_OPERATORS = ['sum', 'prod']
OTHER_OPERATORS = ['in', 'inc', 'nN', 'zZ', 'qQ', 'rR', 'cC', 'forall', 'exists', '*', '<=', '>=', '==>', '<==>', '!=',]

# Operators arguments are strings

def frac(numerator, denominator):
    return f'\\frac{{{numerator}}}{{{denominator}}}'

def lim(variable, variable_limit):
    return f'\\lim_{{{variable} \\to {variable_limit}}}'

def integral(inf, sup):
    return f'\\int_{{{inf}}}^{{{sup}}}'

def sum(index_name, start, end):
    return f'\\sum_{{{index_name} = start}}{{end}}'

def prod(index_name, start, end):
    return f'\\prod_{{{index_name} = start}}{{end}}'