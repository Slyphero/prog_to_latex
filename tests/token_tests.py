import sys
sys.path.append("/media/raphael/externalDisk/perso/GithubPerso/prog_to_latex")

import pytest 
import string_treatment

string_input = 'int a b f(x) x'
token_test = string_treatment.Token(string_input)
token_test_brackets1 = string_treatment.Token('a [ b + c')
token_test_brackets2 = string_treatment.Token('a [ b + c ]')
token_test_brackets3 = string_treatment.Token('[ a + [ b + c ] ]')
token_test_brackets4 = string_treatment.Token('[ a + [ b + c ] ] ]')

def test_token_constructor():
    assert token_test.tokens == ['int', 'a', 'b', 'f(x)', 'x']

def test_validate_brackets1():
    assert token_test_brackets1.verify_brackets() == False

def test_validate_brackets2():
    assert token_test_brackets2.verify_brackets() == True

def test_validate_brackets3():
    assert token_test_brackets3.verify_brackets() == True 

def test_validate_brackets4():
    assert token_test_brackets4.verify_brackets() == False