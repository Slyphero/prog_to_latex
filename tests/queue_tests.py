import sys
sys.path.append("/media/raphael/externalDisk/perso/GithubPerso/prog_to_latex")
sys.path.append("E:\perso\GithubPerso\prog_to_latex")

import queue_class
import pytest

queue_test1 = queue_class.Queue()

def test_queue_is_empty():
    assert queue_test1.is_empty()

queue_test2 = queue_class.Queue()
queue_test2.queue(1)

def test_queue_queue():
    assert queue_test2.keywords == [1]

queue_test3 = queue_class.Queue()
queue_test3.queue(2)

val1 = queue_test3.unqueue()

def test_unqueue1():
    assert val1 == 2

def test_unqueue2():
    assert queue_test3.is_empty()

queue_test4 = queue_class.Queue()
queue_test4.queue(1)
queue_test4.queue(2)

def test_queue_first():
    assert queue_test4.queue_first() == 1

queue_test5 = queue_class.Queue()
queue_test5.queue(1)
queue_test5.queue(2)

queue_test5.empty()

def test_queue_empty():
    assert queue_test5.is_empty()