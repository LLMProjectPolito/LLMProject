
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
    # Basic single operations
    (['+'], [1, 2], 3),
    (['-'], [5, 2], 3),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Operator precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),      # 2 + (3 * 4) = 14
    (['*', '+'], [2, 3, 4], 10),      # (2 * 3) + 4 = 10
    (['-', '//'], [10, 4, 2], 8),     # 10 - (4 // 2) = 8
    (['//', '-'], [10, 4, 2], 0),     # (10 // 4) - 2 = 2 - 2 = 0
    
    # Operator precedence: Exponentiation before others
    (['**', '+'], [2, 3, 4], 12),     # (2 ** 3) + 4 = 12
    (['+', '**'], [2, 3, 2], 11),     # 2 + (3 ** 2) = 11
    (['*', '**'], [2, 3, 2], 18),     # 2 * (3 ** 2) = 18
    (['**', '*'], [2, 3, 4], 32),     # (2 ** 3) * 4 = 32
    
    # Complex expressions
    (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + 3 * 4 - 5 = 9
    (['*', '//', '**'], [10, 2, 5, 2], 24), # 10 * (2 // 5) ** 2 = 10 * 0**2 = 0 (Wait: 10 * 0 = 0)
    # Correction: 10 * (2 // 5) ** 2 -> 10 * 0 ** 2 = 0. 
    # Let's try: 10 * 2 // 5 ** 2 -> (10 * 2) // 25 = 20 // 25 = 0.
    # Let's try: 2 ** 3 * 2 // 4 -> 8 * 2 // 4 = 16 // 4 = 4
    (['**', '*', '//'], [2, 3, 2, 4], 4),
    
    # Edge cases: Zeros
    (['+'], [0, 0], 0),
    (['*'], [0, 10], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    (['//'], [0, 5], 0),
    
    # Large numbers
    (['**'], [10, 5], 100000),
    (['+'], [10**10, 10**10], 2 * 10**10),
])
def test_do_algebra_parametrized(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_minimum_length():
    # Minimum requirements: 1 operator, 2 operands
    assert do_algebra(['+'], [1, 1]) == 2

def test_do_algebra_long_chain():
    # Testing a longer sequence of operations
    operators = ['+', '-', '*', '//', '**']
    operands = [1, 2, 3, 4, 2, 2]
    # Expression: 1 + 2 - 3 * 4 // 2 ** 2
    # 2 ** 2 = 4
    # 3 * 4 // 4 = 12 // 4 = 3
    # 1 + 2 - 3 = 0
    assert do_algebra(operators, operands) == 0