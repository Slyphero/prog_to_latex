import pytest
import operators

# ----- Fractions tests ----- #
def test_frac1():
    assert operators.frac(['a', 'b']) == '\\frac{a}{b}'

def test_frac2():
    assert operators.frac(['\\frac{a}{b}', 'c']) == '\\frac{\\frac{a}{b}}{c}'

def test_frac3():
    assert operators.frac(['\\frac{a}{b}', '\\frac{c}{d}']) == '\\frac{\\frac{a}{b}}{\\frac{c}{d}}'

def test_frac4():
    assert operators.frac(['(a + b)', 'c']) == '\\frac{(a + b)}{c}'
