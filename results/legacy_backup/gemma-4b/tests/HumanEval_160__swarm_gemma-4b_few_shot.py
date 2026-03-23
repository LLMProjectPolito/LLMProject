import pytest
import math

def test_do_algebra_single_operation():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8