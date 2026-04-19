
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

def test_do_algebra_exponentiation_associativity():
    # In Python, the exponentiation operator (**) is right-associative.
    # 2 ** 3 ** 2 should be evaluated as 2 ** (3 ** 2) = 2 ** 9 = 512, 
    # rather than (2 ** 3) ** 2 = 8 ** 2 = 64.
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512

def test_do_algebra_precedence():
    # Tests operator precedence: 1 + (2 * (3 ** 2) // 4) -> 1 + (2 * 9 // 4) -> 1 + (18 // 4) -> 1 + 4 = 5
    assert do_algebra(['+', '*', '**', '//'], [1, 2, 3, 2, 4]) == 5

def test_do_algebra_complex_precedence():
    assert do_algebra(['+', '//', '**'], [1, 2, 2, 3]) == 1