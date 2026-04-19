
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

import pytest
import math

def test_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_zero_edge_case():
    assert do_algebra(['**'], [0, 0]) == 1

import pytest

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])