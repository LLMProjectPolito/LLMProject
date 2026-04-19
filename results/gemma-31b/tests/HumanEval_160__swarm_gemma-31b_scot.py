
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

@pytest.mark.parametrize("operators, operands, expected", [
    # Test: 10 - 2 * 4 // 2 ** 3 -> 10 - (8 // 8) = 9
    (['-', '*', '//', '**'], [10, 2, 4, 2, 3], 9),
    # Test: 5 + 2**3 // 4 -> 5 + (8 // 4) = 7
    (['+', '**', '//'], [5, 2, 3, 4], 7),
    # Test: 1 + 2 * 3 ** 2 // 4 -> 1 + (2 * 9 // 4) -> 1 + 4 = 5
    (['+', '*', '**', '//'], [1, 2, 3, 2, 4], 5),
])
def test_do_algebra_precedence(operators, operands, expected):
    """
    Tests that the function correctly respects Python's operator precedence:
    Exponentiation (**) > Multiplication (*) / Floor Division (//) > Addition (+) / Subtraction (-)
    """
    assert do_algebra(operators, operands) == expected