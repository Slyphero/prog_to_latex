def frac(frac_input):
    keywords = frac_input.split(',')
    return f'\\frac{{{keywords[0]}}}{{{keywords[1]}}}'
    
def lim(lim_input):
    keywords = lim_input.split(',')
    if keywords[4] == "arrow":
        return f'{keywords[2]} \\xrightarrow[{keywords[0]} \\to {keywords[1]}]{{}} {keywords[3]}'
    else:
        return f'\\lim_{{{keywords[1]} \\to {keywords[2]}}} {keywords[0]} = {keywords[3]}'

def sum(sum_input):
    keywords = sum_input.split(',')
    return f'\\sum_{{{keywords[0]}}}^{{{keywords[1]}}} {keywords[2]} = {keywords[3]}'

def prod(prod_input):
    keywords = prod_input.split(',')
    return f'\\prod_{{{keywords[0]}}}^{{{keywords[1]}}} {keywords[2]} = {keywords[3]}'

def int(int_input):
    keywords = int_input.split(',')
    return f'\\int_{{{keywords[0]}}}^{{{keywords[1]}}} {keywords[2]} \\dd{{{keywords[3]}}} = {keywords[4]}'

def root(root_input):
    keywords = root_input.split(',')
    return f'\\sqrt[{keywords[1]}]{{{keywords[0]}}}'