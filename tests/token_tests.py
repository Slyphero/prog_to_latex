import sys
sys.path.append("/media/slyphero/externalDisk/perso/GithubPerso/prog_to_latex")

import pytest 
import tokenize 

string_input = 'int a b f(x) x'
token_test = tokenize.Token(string_input)

def test_token_constructor():
    assert token_test.tokens == ['int', 'a', 'b', 'f(x)', 'x']