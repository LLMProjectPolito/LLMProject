
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
from math_module import do_algebra

@pytest.mark.parametrize("operators, operands, expected", [
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
])
def test_basic_operations(operators, operands, expected):
    """Test each operator individually with simple operands."""
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators, operands, expected", [
    (['+', '*'], [2, 3, 4], 14),      # 2 + (3 * 4)
    (['*', '+'], [2, 3, 4], 10),      # (2 * 3) + 4
    (['*', '**'], [2, 3, 2], 18),     # 2 * (3 ** 2)
    (['+', '**'], [2, 3, 2], 11),     # 2 + (3 ** 2)
    (['-', '**'], [10, 2, 3], 2),     # 10 - (2 ** 3)
    (['//', '*'], [10, 2, 5], 25),    # (10 // 2) * 5
    (['*', '//'], [10, 2, 5], 4),     # (10 * 2) // 5
])
def test_operator_precedence(operators, operands, expected):
    """Test that standard mathematical precedence is respected."""
    assert do_algebra(operators, operands) == expected

def test_complex_expression():
    """Test a long chain of mixed operators."""
    # 2 + 3 * 4 - 5 // 10 ** 2
    # 1. 10**2 = 100
    # 2. 3*4 = 12
    # 3. 5//100 = 0
    # 4. 2 + 12 - 0 = 14
    operators = ['+', '*', '-', '//', '**']
    operands = [2, 3, 4, 5, 10, 2]
    assert do_algebra(operators, operands) == 14

@pytest.mark.parametrize("operators, operands, expected", [
    (['*'], [0, 5], 0),    # Zero as first operand
    (['*'], [5, 0], 0),    # Zero as second operand
    (['**'], [5, 0], 1),   # Zero as exponent
    (['+'], [0, 0], 0),    # Both zero
    (['//'], [5, 10], 0),  # Floor division resulting in zero
])
def test_edge_cases_zero(operators, operands, expected):
    """Test behavior involving zero."""
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators, operands, expected", [
    (['-'], [-5, -2], -3),    # Negative operands
    (['+'], [-10, 5], -5),    # Negative + Positive
    (['**'], [2, -1], 0.5),   # Negative exponent (returns float)
    (['*'], [-2, -3], 6),     # Two negatives
])
def test_negative_numbers(operators, operands, expected):
    """Test behavior with negative operands and exponents."""
    assert do_algebra(operators, operands) == expected

def test_complex_number_result():
    """Test that negative numbers raised to fractional powers return complex numbers."""
    # (-4) ** 0.5 = 2j
    operators = ['**']
    operands = [-4, 0.5]
    result = do_algebra(operators, operands)
    assert isinstance(result, complex)
    assert result == 2j

@pytest.mark.parametrize("operators, operands, expected", [
    (['+', '*', '**'], [0.1, 0.2, 2, 0.5], 0.1 + (0.2 * 1.41421356)),
    (['+', '//', '**'], [10.5, 2, 3, 0.5], 10.5 + (1.0 * 1.73205081)),
])
def test_floating_point_chains(operators, operands, expected):
    """Test cumulative floating-point precision in complex chains."""
    assert do_algebra(operators, operands) == pytest.approx(expected)

def test_division_by_zero_in_chains():
    """Test that ZeroDivisionError propagates from the middle of a chain."""
    # 10 * (5 // 0) * 2
    operators = ['*', '//', '*']
    operands = [10, 5, 0, 2]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operators, operands)

def test_overflow_handling():
    """Test that extremely large float calculations raise OverflowError."""
    # 10.0 to the power of 1000 is too large for a float
    operators = ['**']
    operands = [10.0, 1000.0]
    with pytest.raises(OverflowError):
        do_algebra(operators, operands)

@pytest.mark.parametrize("operators, operands", [
    (['+', '*'], [1, 2]),          # Too many operators (len 2 vs len 1)
    (['+'], [1, 2, 3]),            # Too many operands (len 3 vs len 1)
    ([], []),                      # Empty lists
])
def test_mismatched_lengths(operators, operands):
    """Test that mismatched operator/operand lengths raise errors."""
    # Depending on implementation, this could be ValueError or IndexError
    with pytest.raises((ValueError, IndexError)):
        do_algebra(operators, operands)

@pytest.mark.parametrize("operators, operands", [
    (['%'], [10, 5]),              # Unsupported operator
    (['add'], [10, 5]),            # Unsupported operator string
])
def test_unsupported_operator(operators, operands):
    """Test that unsupported operators raise a ValueError."""
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

@pytest.mark.parametrize("operators, operands", [
    (['+'], [1, 'a']),             # Non-numeric operand
    (['*'], [1, None]),            # NoneType operand
])
def test_invalid_operand_types(operators, operands):
    """Test that non-numeric operands raise a TypeError."""
    with pytest.raises(TypeError):
        do_algebra(operators, operands)

@pytest.mark.parametrize("operators, operands", [
    (None, [1, 2]),                # Operator is not a list
    (['+'], "not a list"),         # Operands is not a list
    (123, 456),                    # Both are not lists
])
def test_invalid_input_types(operators, operands):
    """Test that non-list inputs raise a TypeError."""
    with pytest.raises(TypeError):
        do_algebra(operators, operands)

def test_large_integers():
    """Test with larger integers to ensure no overflow issues (Python ints are arbitrary precision)."""
    assert do_algebra(['**'], [10, 10]) == 10000000000

def test_minimum_input():
    """Test the smallest possible valid input."""
    assert do_algebra(['+'], [1, 1]) == 2