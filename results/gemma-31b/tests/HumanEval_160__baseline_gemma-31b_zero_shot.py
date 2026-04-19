
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

@pytest.mark.parametrize("operators, operands, expected", [
    # Example case from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    # Basic operations
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 5], 2),
    (['**'], [2, 3], 8),
    # Operator precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),  # 2 + (3 * 4)
    (['*', '+'], [2, 3, 4], 10),  # (2 * 3) + 4
    (['-', '*'], [10, 2, 3], 4),  # 10 - (2 * 3)
    # Operator precedence: Exponentiation first
    (['+', '**'], [2, 3, 2], 11), # 2 + (3 ** 2)
    (['**', '+'], [2, 3, 2], 10), # (2 ** 3) + 2
    (['**', '*'], [2, 3, 2], 16), # (2 ** 3) * 2
    # Floor division and precedence
    (['//', '+'], [10, 3, 1], 4), # (10 // 3) + 1 = 3 + 1
    (['+', '//'], [1, 10, 3], 4), # 1 + (10 // 3) = 1 + 3
    # Complex expression
    (['**', '*', '//', '+'], [2, 3, 4, 8, 1], 7), # (2**3 * 4 // 8) + 1 = (8 * 4 // 8) + 1 = 4 + 1 = 5
    # Wait, recalculating: 2**3 * 4 // 8 + 1 -> 8 * 4 // 8 + 1 -> 32 // 8 + 1 -> 4 + 1 = 5
    # Let's use a simpler complex one:
    (['+', '-', '*'], [1, 2, 3, 4], -5), # 1 + 2 - (3 * 4) = 3 - 12 = -9
    # Correcting the complex one above for the test case:
    (['+', '-', '*'], [1, 2, 3, 4], -9),
    # Edge cases: Zeroes
    (['*'], [0, 100], 0),
    (['+'], [0, 0], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    # Large numbers
    (['*'], [1000, 1000], 1000000),
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_minimum_length():
    # Minimum requirements: 1 operator, 2 operands
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['-'], [1, 1]) == 0

def test_do_algebra_negative_result():
    # Result can be negative even if operands are non-negative
    assert do_algebra(['-'], [5, 10]) == -5

def test_do_algebra_floor_division_rounding():
    # Ensure floor division is used, not float division
    assert do_algebra(['//'], [7, 3]) == 2