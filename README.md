# prog_to_latex
Pseudo-code to LaTeX code

## Syntax 
To quit the program, type `quit` and press `Enter`.  

|Pseudo-code|LaTeX Code|
|-|-|
|frac,a,b|\frac{a}{b}|
|sum,k=m,n,a_n,a_m + \cdots + a_n|\sum_{k=m}^{n} a_n = a_m + \cdots + a_n|
|prod,k=m,n,a_n,a_m + \cdots + a_n|\prod_{k=m}^{n} a_n = a_m + \cdots + a_n|
|lim,x,a,f(x),l,lim|\lim_{x \to a} f(x) = l 
|lim,x,a,f(x),l,arrow|f(x) \xrightarrow[x \to a]{} l

## Issues
Cannot nest fractions, sums, products yet.