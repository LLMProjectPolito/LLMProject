
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
    (['+', '*'], [2, 3, 4], 14),  # 2 + (3 * 4)
    (['*', '+'], [2, 3, 4], 10),  # (2 * 3) + 4
    (['-', '//'], [10, 5, 2], 8), # 10 - (5 // 2) = 10 - 2
    (['//', '-'], [10, 5, 2], 0), # (10 // 5) - 2 = 2 - 2
    
    # Operator precedence: Exponentiation before Multiplication/Division
    (['*', '**'], [2, 3, 4], 162), # 2 * (3 ** 4) = 2 * 81
    (['**', '*'], [2, 3, 4], 32),  # (2 ** 3) * 4 = 8 * 4
    (['//', '**'], [100, 2, 3], 12), # 100 // (2 ** 3) = 100 // 8 = 12
    
    # Right-associativity of exponentiation
    (['**', '**'], [2, 2, 3], 256), # 2 ** (2 ** 3) = 2 ** 8 = 256
    
    # Complex expressions (Example from docstring)
    (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
    
    # Edge cases: Zeroes and Large Numbers
    (['+', '*'], [0, 0, 0], 0),
    (['*', '+'], [0, 10, 5], 5),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    (['*'], [1000, 1000], 1000000),
    
    # Long chain of same precedence
    (['+', '+', '+'], [1, 1, 1, 1], 4),
    (['-', '-', '-'], [10, 2, 2, 2], 4),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    (['//', '//'], [100, 5, 2], 10), # (100 // 5) // 2 = 20 // 2 = 10
])
def test_do_algebra_scenarios(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_minimum_input():
    # Minimum requirements: 1 operator, 2 operands
    assert do_algebra(['+'], [1, 1]) == 2

def test_do_algebra_large_exponent():
    # Testing a reasonably large result
    assert do_algebra(['**'], [2, 10]) == 1024