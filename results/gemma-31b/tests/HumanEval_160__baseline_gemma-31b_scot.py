
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

def test_basic_operations():
    """Test each operator in isolation."""
    assert do_algebra(['+'], [10, 5]) == 15
    assert do_algebra(['-'], [10, 5]) == 5
    assert do_algebra(['*'], [10, 5]) == 50
    assert do_algebra(['//'], [10, 5]) == 2
    assert do_algebra(['**'], [2, 3]) == 8

def test_operator_precedence():
    """Test that Python's operator precedence is maintained."""
    # 2 + (3 * 4) = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14
    # (2 * 3) + 4 = 10 (but precedence is 2 * 3 + 4)
    assert do_algebra(['*', '+'], [2, 3, 4]) == 10
    # 2 * (3 ** 2) = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    # (2 ** 3) * 2 = 16
    assert do_algebra(['**', '*'], [2, 3, 2]) == 16
    # 10 - 2 // 2 = 10 - 1 = 9
    assert do_algebra(['-', '//'], [10, 2, 2]) == 9

def test_example_case():
    """Test the specific example provided in the problem description."""
    # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_minimum_input():
    """Test the smallest valid input size."""
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['-'], [1, 1]) == 0

def test_zero_handling():
    """Test cases involving zero as an operand."""
    # 0 * 5 + 0 = 0
    assert do_algebra(['*', '+'], [0, 5, 0]) == 0
    # 5 + 0 ** 2 = 5 + 0 = 5
    assert do_algebra(['+', '**'], [5, 0, 2]) == 5
    # 0 ** 5 = 0
    assert do_algebra(['**'], [0, 5]) == 0
    # 5 ** 0 = 1
    assert do_algebra(['**'], [5, 0]) == 1

def test_floor_division_details():
    """Test floor division specifically for rounding and zero results."""
    # 1 // 2 = 0
    assert do_algebra(['//'], [1, 2]) == 0
    # 11 // 3 = 3
    assert do_algebra(['//'], [11, 3]) == 3

def test_large_values():
    """Test with larger integers and exponents."""
    # 10 ** 5 = 100000
    assert do_algebra(['**'], [10, 5]) == 100000
    # 100 * 100 + 100 = 10100
    assert do_algebra(['*', '+'], [100, 100, 100]) == 10100

def test_complex_chain():
    """Test a longer chain of various operators."""
    # 2 ** 3 + 10 // 3 * 2 - 1
    # 8 + 3 * 2 - 1
    # 8 + 6 - 1 = 13
    assert do_algebra(['**', '+', '//', '*', '-'], [2, 3, 10, 3, 2, 1]) == 13