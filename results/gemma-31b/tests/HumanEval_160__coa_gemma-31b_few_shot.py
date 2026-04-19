
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
    # Mixed precedence: Exponentiation -> Multiplication -> Addition
    # 1 + 2 * 3 ** 2 = 1 + 2 * 9 = 1 + 18 = 19
    assert do_algebra(['+', '*', '**'], [1, 2, 3, 2]) == 19

# Focus: Boundary Values
def test_do_algebra_min_length_min_values():
    # Minimum allowed length (1 operator, 2 operands) and minimum non-negative integer values
    assert do_algebra(['+'], [0, 0]) == 0

def test_do_algebra_min_length_exponent_zero():
    # Minimum length with exponentiation boundary (any number to power of 0 is 1)
    assert do_algebra(['**'], [10, 0]) == 1

def test_do_algebra_min_length_floor_div_zero_numerator():
    # Minimum length with floor division boundary (0 divided by any positive integer is 0)
    assert do_algebra(['//'], [0, 5]) == 0

# Focus: Operator Combinations
import pytest

def test_operator_combinations_precedence():
    # Tests mixed precedence: Multiplication before Addition
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14  # 2 + (3 * 4)
    # Tests mixed precedence: Exponentiation before Multiplication and Subtraction
    assert do_algebra(['**', '*', '-'], [2, 3, 2, 1]) == 15  # (2**3) * 2 - 1 = 8 * 2 - 1

def test_operator_combinations_floor_div():
    # Tests Floor Division combined with Addition
    assert do_algebra(['//', '+'], [10, 3, 5]) == 8  # (10 // 3) + 5 = 3 + 5
    # Tests Floor Division combined with Multiplication
    assert do_algebra(['*', '//'], [2, 5, 3]) == 3  # (2 * 5) // 3 = 10 // 3

def test_operator_combinations_complex():
    # Tests a combination of all operators to ensure correct Python evaluation order
    # Expression: 2 ** 3 + 10 // 3 * 2 - 1
    # Order: (2**3) + ((10//3) * 2) - 1 = 8 + (3 * 2) - 1 = 8 + 6 - 1 = 13
    assert do_algebra(['**', '+', '//', '*', '-'], [2, 3, 10, 3, 2, 1]) == 13