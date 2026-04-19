
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

def test_do_algebra_precedence_mul_add():
    # Multiplication should be evaluated before addition
    # 2 + 3 * 4 = 2 + 12 = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14
    # 10 - 2 * 3 = 10 - 6 = 4
    assert do_algebra(['-', '*'], [10, 2, 3]) == 4

def test_do_algebra_precedence_exp_mul_div():
    # Exponentiation should be evaluated before multiplication/division
    # 2 * 3 ** 2 = 2 * 9 = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    # 10 // 2 ** 2 = 10 // 4 = 2
    assert do_algebra(['//', '**'], [10, 2, 2]) == 2

def test_do_algebra_precedence_complex_mix():
    # Mixed precedence: ** then * // then + -
    # 2 + 3 * 2 ** 3 - 10 // 3
    # 2 + 3 * 8 - 3
    # 2 + 24 - 3 = 23
    assert do_algebra(['+', '*', '**', '-', '//'], [2, 3, 2, 3, 10, 3]) == 23

# Focus: Boundary Values
def test_do_algebra_min_constraints():
    # Minimum length of operator (1) and operand (2) with minimum possible values (0)
    assert do_algebra(['+'], [0, 0]) == 0

def test_do_algebra_boundary_zero_operands():
    # Testing boundary cases with 0: 0**0 and 0 // x
    assert do_algebra(['**'], [0, 0]) == 1
    assert do_algebra(['//'], [0, 10]) == 0

def test_do_algebra_boundary_negative_result():
    # Testing boundary where non-negative operands result in a negative value
    assert do_algebra(['-'], [0, 1]) == -1

# Focus: Error Scenarios
import pytest

def test_do_algebra_division_by_zero():
    """Test that floor division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_mismatched_lengths():
    """Test that mismatched lengths of operators and operands raise an error."""
    with pytest.raises((ValueError, IndexError)):
        do_algebra(['+'], [1, 2, 3])

def test_do_algebra_invalid_operator():
    """Test that an unsupported operator raises an error."""
    with pytest.raises((SyntaxError, ValueError, KeyError)):
        do_algebra(['%'], [10, 2])