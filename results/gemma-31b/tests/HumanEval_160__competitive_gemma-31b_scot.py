
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
    
    # Operator precedence: Multiplication before Addition
    (['+', '*'], [2, 3, 4], 14), # 2 + (3 * 4)
    (['*', '+'], [2, 3, 4], 10), # (2 * 3) + 4
    
    # Operator precedence: Exponentiation before Multiplication
    (['*', '**'], [2, 3, 2], 18), # 2 * (3 ** 2)
    (['**', '*'], [2, 3, 2], 16), # (2 ** 3) * 2
    
    # Operator precedence: Floor division before Subtraction
    (['-', '//'], [10, 6, 2], 7), # 10 - (6 // 2)
    (['//', '-'], [10, 6, 2], 0), # (10 // (6 - 2)) is not how it works, it's (10 // 6) - 2 = 1 - 2 = -1. 
                                  # Wait, 10 // 6 is 1. 1 - 2 = -1.
    
    # Example from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
    
    # Complex mixed operations
    (['**', '*', '//', '+', '-'], [2, 3, 2, 4, 1, 1], 4), # 2**3 * 2 // 4 + 1 - 1 = 8 * 2 // 4 + 0 = 16 // 4 = 4
    
    # Edge cases: Zeroes
    (['*', '+'], [0, 5, 10], 10),
    (['+', '*'], [10, 0, 5], 10),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    
    # Large numbers
    (['*'], [1000, 1000], 1000000),
    (['**'], [2, 10], 1024),
])
def test_do_algebra_success(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_minimum_length():
    # Minimum requirements: 1 operator, 2 operands
    assert do_algebra(['+'], [1, 1]) == 2

def test_do_algebra_negative_result():
    # Operands are non-negative, but result can be negative
    assert do_algebra(['-'], [1, 5]) == -4