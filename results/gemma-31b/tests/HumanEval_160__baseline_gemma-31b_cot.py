
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

def test_do_algebra_basic_operations():
    """Test basic single-operator cases."""
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-'], [10, 5]) == 5
    assert do_algebra(['*'], [3, 4]) == 12
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_example_case():
    """Test the example provided in the docstring."""
    # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_precedence():
    """Test that Python's operator precedence is respected (PEMDAS)."""
    # Multiplication before addition: 2 + 3 * 4 = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14
    # Addition before multiplication: 2 * 3 + 4 = 10
    assert do_algebra(['*', '+'], [2, 3, 4]) == 10
    # Exponentiation before multiplication: 2 * 3 ** 2 = 2 * 9 = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    # Exponentiation before addition: 2 ** 3 + 4 = 8 + 4 = 12
    assert do_algebra(['**', '+'], [2, 3, 4]) == 12
    # Addition before exponentiation: 2 + 3 ** 2 = 2 + 9 = 11
    assert do_algebra(['+', '**'], [2, 3, 2]) == 11

def test_do_algebra_left_to_right():
    """Test operators with the same precedence are evaluated left-to-right."""
    # Floor division and multiplication have same precedence: 10 // 2 * 5 = 5 * 5 = 25
    assert do_algebra(['//', '*'], [10, 2, 5]) == 25
    # 10 * 2 // 5 = 20 // 5 = 4
    assert do_algebra(['*', '//'], [10, 2, 5]) == 4
    # 10 - 5 + 2 = 5 + 2 = 7
    assert do_algebra(['-', '+'], [10, 5, 2]) == 7

def test_do_algebra_edge_values():
    """Test edge cases like zero, negative results, and large exponents."""
    # Result is negative
    assert do_algebra(['-'], [2, 5]) == -3
    # Floor division resulting in zero
    assert do_algebra(['//'], [1, 2]) == 0
    # Exponentiation with zero
    assert do_algebra(['**'], [5, 0]) == 1
    assert do_algebra(['**'], [0, 5]) == 0
    # Large numbers
    assert do_algebra(['**', '*'], [2, 10, 2]) == 2048 # (2**10) * 2

def test_do_algebra_complex_expression():
    """Test a longer sequence of mixed operators."""
    # 2 ** 3 + 10 // 3 * 2 - 1
    # 8 + 3 * 2 - 1
    # 8 + 6 - 1 = 13
    assert do_algebra(['**', '+', '//', '*', '-'], [2, 3, 10, 3, 2, 1]) == 13

def test_do_algebra_division_by_zero():
    """Test that division by zero raises the appropriate Python exception."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

@pytest.mark.parametrize("ops, nums, expected", [
    (['+'], [0, 0], 0),
    (['*'], [0, 100], 0),
    (['-'], [0, 0], 0),
    (['**'], [0, 0], 1), # 0**0 is 1 in Python
    (['//'], [0, 5], 0),
])
def test_do_algebra_zero_operands(ops, nums, expected):
    """Parametrized tests for various zero-operand scenarios."""
    assert do_algebra(ops, nums) == expected