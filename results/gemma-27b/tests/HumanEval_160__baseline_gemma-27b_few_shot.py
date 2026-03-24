
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

def test_algebra_basic():
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

def test_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_algebra_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_algebra_complex():
    assert do_algebra(['+', '*', '-', '//'], [2, 3, 4, 5, 2]) == 2 + 3 * 4 - 5 // 2

def test_algebra_multiple_operators():
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2]) == 1 + 2 - 3 * 4 // 5 ** 2

def test_algebra_long_expression():
    assert do_algebra(['+', '+', '+', '+', '+'], [1, 2, 3, 4, 5, 6]) == 21

def test_algebra_with_zero():
    assert do_algebra(['*'], [5, 0]) == 0

def test_algebra_division_by_one():
    assert do_algebra(['//'], [10, 1]) == 10

def test_algebra_exponentiation_zero():
    assert do_algebra(['**'], [2, 0]) == 1

def test_algebra_exponentiation_one():
    assert do_algebra(['**'], [5, 1]) == 5