import pytest
import math


# Focus: Operator Validation
def test_do_algebra_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_multiplication():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_do_algebra_complex():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

# Focus: Operand Value Range
import pytest

def test_do_algebra_operand_range_positive():
    assert do_algebra(['+', '*'], [1, 2, 3]) == 7
    assert do_algebra(['-', '//'], [10, 2]) == 8
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_operand_range_zero():
    assert do_algebra(['+', '*'], [0, 2, 3]) == 6
    assert do_algebra(['-', '//'], [10, 0]) == pytest.raises(ZeroDivisionError)
    assert do_algebra(['**'], [0, 3]) == 0

def test_do_algebra_operand_range_large():
    assert do_algebra(['+', '*'], [100, 200, 300]) == 700
    assert do_algebra(['-', '//'], [1000, 100]) == 900
    assert do_algebra(['**'], [2, 10]) == 1024

# Focus: Expression Complexity
import pytest
from your_module import do_algebra  # Replace your_module

def test_do_algebra_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_multiplication():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_do_algebra_complex():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9