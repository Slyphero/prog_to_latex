import sys
sys.path.append("/media/raphael/externalDisk/perso/GithubPerso/prog_to_latex")
sys.path.append("E:\perso\GithubPerso\prog_to_latex")

import pytest 
import stack

stack_test1 = stack.Stack()

def test_stack_is_empty():
    assert stack_test1.is_empty

stack_test2 = stack.Stack()
stack_test2.stack(2)

def test_stack_stack():
    assert stack_test2.keywords == [2]

stack_test3 = stack.Stack()
stack_test3.stack(2)
stack_test3.stack(3)

def test_stack_stack_top():
    assert stack_test3.stack_top() == 3

stack_test4 = stack.Stack()
stack_test4.stack(2)
stack_test4.stack(3)

val1 = stack_test4.unstack()

def test_stack_unstack1():
    assert val1 == 3

def test_stack_unstack2():
    assert stack_test4.keywords == [2]

stack_test5 = stack.Stack()
stack_test5.stack(3)
stack_test5.stack(5)

stack_test5.empty()

def test_stack_empty():
    assert stack_test5.is_empty()    


