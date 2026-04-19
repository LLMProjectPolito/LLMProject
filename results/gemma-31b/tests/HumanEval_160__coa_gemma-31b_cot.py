
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


# Focus: Operator Precedence
import pytest

def test_operator_precedence_mul_add():
    # Multiplication should be evaluated before addition
    # 2 + 3 * 4 = 2 + 12 = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

def test_operator_precedence_exp_mul():
    # Exponentiation should be evaluated before multiplication
    # 2 * 3 ** 2 = 2 * 9 = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18

def test_operator_precedence_complex():
    # Mixed precedence: Exponentiation > Multiplication > Addition
    # 2 + 3 * 2 ** 3 = 2 + 3 * 8 = 2 + 24 = 26
    assert do_algebra(['+', '*', '**'], [2, 3, 2, 3]) == 26

# Focus: Boundary Values
def test_do_algebra_min_length_and_values():
    # Boundary: Minimum allowed length of operator (1) and operand (2) lists, 
    # and minimum allowed operand values (0).
    assert do_algebra(['+'], [0, 0]) == 0

def test_do_algebra_floor_div_boundary():
    # Boundary: Floor division where the result is 0 (numerator < denominator).
    assert do_algebra(['//'], [1, 2]) == 0

def test_do_algebra_negative_result_boundary():
    # Boundary: Minimum operand values resulting in a negative integer.
    assert do_algebra(['-'], [0, 1]) == -1

# Focus: Error Scenarios
import pytest

def test_do_algebra_division_by_zero():
    """Test that floor division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_invalid_operand_type():
    """Test that providing non-integer operands raises a TypeError."""
    with pytest.raises(TypeError):
        do_algebra(['+'], [10, '5'])

def test_do_algebra_mismatched_lengths():
    """Test that mismatched operator and operand lengths raise an error."""
    with pytest.raises((IndexError, ValueError, TypeError)):
        do_algebra(['+', '*'], [10])