# For all functions in this file : keywords is a str list

def frac(keywords):
    return f'\\frac{{{keywords[0]}}}{{{keywords[1]}}}'

def plus(keywords) : 
    return f'{keywords[0]} + {keywords[1]}'

def minus(keywords):
    return f'{keywords[0]} - {keywords[1]}'

def times(keywords):
    return f'{keywords[0]} \cdot {keywords[1]}'

def neq(keywords):
    return f'{keywords[0]} \\neq {keywords[1]}'

def geq(keywords):
    return f'{keywords[0]} \\geqslant {keywords[1]}'

def leq(keywords):
    return f'{keywords[0]} \\leqslant {keywords[1]}'