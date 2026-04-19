
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

def test_do_algebra_exponent_associativity():
    # Tests the right-associativity of the exponentiation operator (**)
    # In Python, 2 ** 2 ** 3 is evaluated as 2 ** (2 ** 3) = 2 ** 8 = 256,
    # not (2 ** 2) ** 3 = 4 ** 3 = 64.
    assert do_algebra(['**', '**'], [2, 2, 3]) == 256

def test_do_algebra_precedence():
    # Tests operator precedence: Exponentiation (**) first, then Floor Division (//), then Subtraction (-)
    # Expression: 5 - 2 ** 3 // 4 => 5 - 8 // 4 => 5 - 2 => 3
    assert do_algebra(['-', '**', '//'], [5, 2, 3, 4]) == 3