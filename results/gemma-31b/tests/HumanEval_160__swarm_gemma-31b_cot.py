
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
    (['-', '*', '**'], [10, 2, 3, 2], -8),
    (['**', '//', '-'], [2, 3, 4, 5], -3),
    (['**', '//', '-'], [2, 2, 8, 5], -5),
])
def test_do_algebra_precedence_and_negative_results(operators, operands, expected):
    """
    Tests operator precedence (Exponentiation > Multiplication/Division > Addition/Subtraction)
    and verifies that the function correctly handles negative results.
    """
    assert do_algebra(operators, operands) == expected