import pytest

from structures.stack import Stack


def test_new_stack_is_zero():
    new_stack = Stack()
    assert new_stack.__len__() == 0


def test_add_new_node_in_stack():
    new_stack = Stack()
    new_stack.push(1)
    assert new_stack.__len__() == 1


def test_pop_node():
    new_stack = Stack()
    for i in range(11):
        new_stack.push(i)
    assert new_stack.pop() == 10
    assert new_stack.pop() == 9
    assert new_stack.__len__() == 9


def test_continuous_pop():
    new_stack = Stack()
    for i in range(11):
        new_stack.push(i)
    for j in range(5):
        new_stack.pop()
    assert new_stack.pop() == 5


def test_empty_stack():
    new_stack = Stack()
    with pytest.raises(IndexError):
        new_stack.pop()
