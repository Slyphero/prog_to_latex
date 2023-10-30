def frac(frac_input):
    keywords = frac_input.split(',')
    print(f'\\frac{{{keywords[0]}}}{{{keywords[1]}}}')
    
def lim(lim_input):
    keywords = lim_input.split(',')
    match keywords[4]:
        case "arrow":
            print(f'{keywords[2]} \\xrightarrow[{keywords[0]} \\to {keywords[1]}]{{}} {keywords[3]}')
        case "lim":
            print(f'\\lim_{{{keywords[1]} \\to {keywords[2]}}} {keywords[0]} = {keywords[3]}')

def sum(sum_input):
    keywords = sum_input.split(',')
    print(f'\\sum_{{{keywords[0]}}}^{{{keywords[1]}}} {keywords[2]} = {keywords[3]}')

def prod(prod_input):
    keywords = prod_input.split(',')
    print(f'\\prod_{{{keywords[0]}}}^{{{keywords[1]}}} {keywords[2]} = {keywords[3]}')