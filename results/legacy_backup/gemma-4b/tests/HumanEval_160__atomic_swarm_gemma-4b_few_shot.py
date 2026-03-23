import pytest
import math

def test_do_algebra_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_addition():
    operator = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_addition():
    operator = ['+', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 14