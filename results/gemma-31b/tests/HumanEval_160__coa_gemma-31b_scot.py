
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
    # 2 + 3 * 4 = 14 (not 20)
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

def test_operator_precedence_exp_mul():
    # Exponentiation should be evaluated before multiplication
    # 2 * 3 ** 2 = 18 (not 36)
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18

def test_operator_precedence_complex():
    # Mixed precedence: ** then * and // then +
    # 1 + 2 * 3 ** 2 // 4 
    # 1 + 2 * 9 // 4
    # 1 + 18 // 4
    # 1 + 4 = 5
    assert do_algebra(['+', '*', '**', '//'], [1, 2, 3, 2, 4]) == 5

# Focus: Boundary Values
def test_do_algebra_minimum_length_zeros():
    # Boundary: Minimum allowed length (1 operator, 2 operands) with minimum non-negative integers
    assert do_algebra(['+'], [0, 0]) == 0

def test_do_algebra_minimum_length_exponent_boundary():
    # Boundary: Minimum length with exponentiation involving zero
    assert do_algebra(['**'], [0, 0]) == 1

def test_do_algebra_minimum_length_division_boundary():
    # Boundary: Minimum length with floor division resulting in zero
    assert do_algebra(['//'], [1, 2]) == 0

# Focus: Error Scenarios
import pytest

def test_do_algebra_zero_division():
    """Test that floor division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_invalid_operand_type():
    """Test that non-integer operands raise a TypeError."""
    with pytest.raises(TypeError):
        do_algebra(['+'], [10, 'a'])

def test_do_algebra_mismatched_length():
    """Test that mismatched lengths between operators and operands raise an IndexError."""
    with pytest.raises(IndexError):
        do_algebra(['+'], [1])