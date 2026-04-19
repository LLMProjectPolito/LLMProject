
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
    # Example from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + (3 * 4) - 5 = 9
    
    # Basic single operator cases
    (['+'], [1, 2], 3),
    (['-'], [10, 4], 6),
    (['*'], [3, 7], 21),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Operator Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),    # 2 + (3 * 4) = 14
    (['*', '+'], [2, 3, 4], 10),    # (2 * 3) + 4 = 10
    (['-', '//'], [20, 10, 3], 17), # 20 - (10 // 3) = 17
    (['//', '-'], [20, 10, 3], -1), # (20 // 10) - 3 = -1
    (['-', '//'], [10, 4, 2], 8),   # 10 - (4 // 2) = 8
    (['//', '-'], [10, 4, 2], 0),   # (10 // 4) - 2 = 0
    
    # Operator Precedence: Exponentiation before others
    (['+', '**'], [2, 3, 2], 11),   # 2 + (3 ** 2) = 11
    (['**', '+'], [2, 3, 2], 10),   # (2 ** 3) + 2 = 10
    (['*', '**'], [2, 3, 2], 18),   # 2 * (3 ** 2) = 18
    (['**', '*'], [2, 3, 2], 16),   # (2 ** 3) * 2 = 16
    
    # Complex mixed cases
    (['*', '**', '-', '//'], [2, 3, 2, 10, 3], 15), # 2 * (3**2) - (10 // 3) = 18 - 3 = 15
    (['**', '+', '//', '*', '-'], [2, 3, 10, 3, 2, 1], 13), # 8 + (3 * 2) - 1 = 13
    (['**', '//', '+'], [2, 3, 4, 1], 3), # (8 // 4) + 1 = 3
    
    # Repeated operators
    (['+', '+', '+'], [1, 1, 1, 1], 4),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    (['-', '-', '-'], [10, 2, 2, 2], 4),
    
    # Edge cases: Zeroes
    (['*', '+'], [0, 5, 10], 10),   # (0 * 5) + 10 = 10
    (['+', '*'], [0, 5, 10], 50),   # 0 + (5 * 10) = 50
    (['+', '*'], [5, 0, 10], 5),    # 5 + (0 * 10) = 5
    (['**'], [0, 5], 0),            # 0 ** 5 = 0
    (['**'], [5, 0], 1),            # 5 ** 0 = 1
    (['//'], [0, 5], 0),            # 0 // 5 = 0
    
    # Large values
    (['**', '//'], [2, 10, 100], 10), # 1024 // 100 = 10
    (['**', '+'], [2, 10, 5], 1029),  # 1024 + 5 = 1029
    (['**', '*'], [2, 10, 2], 2048),  # 1024 * 2 = 2048
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_minimum_input():
    """Test the smallest possible valid inputs."""
    assert do_algebra(['+'], [0, 0]) == 0
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['-'], [1, 1]) == 0

def test_do_algebra_long_sequence():
    """Test a longer sequence of operations."""
    # 1 + 2 * 3**2 - 4 // 2 = 1 + 18 - 2 = 17
    operators = ['+', '*', '**', '-', '//']
    operands = [1, 2, 3, 2, 4, 2]
    assert do_algebra(operators, operands) == 17

def test_do_algebra_floor_division_precision():
    """Ensure floor division is used, not float division."""
    assert do_algebra(['//'], [7, 2]) == 3

def test_do_algebra_precedence_complex():
    """Test complex precedence: ** then //, *, then +, -"""
    # 2 ** 3 * 2 // 4 + 1 - 1
    # 8 * 2 // 4 + 1 - 1
    # 16 // 4 + 1 - 1
    # 4 + 1 - 1 = 4
    ops = ['**', '*', '//', '+', '-']
    nums = [2, 3, 2, 4, 1, 1]
    assert do_algebra(ops, nums) == 4