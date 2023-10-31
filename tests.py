import pytest
import operators
import compute
import queue
import stack

# ----- Queue tests ----- #
queue_test1 = queue.Queue()

def test_queue_is_empty():
    assert queue_test1.is_empty()

queue_test2 = queue.Queue()
queue_test2.queue(1)

def test_queue_queue():
    assert queue_test2.keywords == [1]
# ----- Stack tests ----- #

# ----- Fractions tests ----- #
def test_frac1():
    assert operators.frac(['a', 'b']) == '\\frac{a}{b}'

def test_frac2():
    assert operators.frac(['\\frac{a}{b}', 'c']) == '\\frac{\\frac{a}{b}}{c}'

def test_frac3():
    assert operators.frac(['\\frac{a}{b}', '\\frac{c}{d}']) == '\\frac{\\frac{a}{b}}{\\frac{c}{d}}'

def test_frac4():
    assert operators.frac(['(a + b)', 'c']) == '\\frac{(a + b)}{c}'
