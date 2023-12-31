import sys
sys.path.append("/media/raphael/externalDisk/perso/GithubPerso/prog_to_latex")
sys.path.append("E:\perso\GithubPerso\prog_to_latex")
sys.path.append("~/Documents/prog_to_latex")

import pytest
import operators

# ----- Fractions tests ----- #
def test_frac1():
    assert operators.frac('a', 'b') == '\\frac{a}{b}'

def test_frac2():
    assert operators.frac('\\frac{a}{b}', 'c') == '\\frac{\\frac{a}{b}}{c}'

def test_frac3():
    assert operators.frac('\\frac{a}{b}', '\\frac{c}{d}') == '\\frac{\\frac{a}{b}}{\\frac{c}{d}}'

def test_frac4():
    assert operators.frac('\\left(a + b\\right)', 'c') == '\\frac{\\left(a + b\\right)}{c}'

# ----- Limits tests ----- #
def test_limit1():
    assert operators.lim('x', 'a') == '\\lim_{x \\to a}'

def test_integral1():
    assert operators.integral('a', 'b') == '\\int_{a}^{b}'

