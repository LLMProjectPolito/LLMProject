import pytest
import math

def test_do_algebra_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_single_operand():
    assert do_algebra(['+'], [5]) is None

def test_do_algebra_invalid_operator():
    assert do_algebra(['%'], [1, 2]) == None