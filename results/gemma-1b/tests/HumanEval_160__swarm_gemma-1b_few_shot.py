
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

def do_algebra(a, b):
    assert math.isclose(a + b, b*b)
    assert math.isclose(a - b, b*b)
    assert math.isclose(a * b, b*b)
    assert math.isclose(a / b, b)
    assert math.isclose(a % b, b)
    assert math.isclose(a ** b, b * b)
    assert math.isclose(a ** b, b)

def test_algebra():
    assert do_algebra('+', '2') == 2
    assert do_algebra('-', '3') == 3
    assert do_algebra('*', '4') == 4
    assert do_algebra('/', '5') == 5
    assert do_algebra('//', '2') == 1
    assert do_algebra('**', '3') == 9

def test_algebra():
    assert do_algebra('+', '2') == 2
    assert do_algebra('-', '3') == 3
    assert do_algebra('*', '4') == 4
    assert do_algebra('/', '5') == 5
    assert do_algebra('//', '2') == 1
    assert do_algebra('**', '3') == 9

def test_algebra():
    assert do_algebra('+', '2') == 2
    assert do_algebra('-', '3') == 3
    assert do_algebra('*', '4') == 4
    assert do_algebra('/', '5') == 5
    assert do_algebra('//', '10') == 10
    assert do_algebra('**', '2') == 2