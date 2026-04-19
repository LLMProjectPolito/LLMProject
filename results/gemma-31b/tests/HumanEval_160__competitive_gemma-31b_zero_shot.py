
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
    # Basic operations
    (['+'], [1, 2], 3),
    (['-'], [10, 2], 8),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Example from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    
    # Operator precedence: Multiplication before Addition
    (['+', '*'], [2, 3, 4], 14), # 2 + (3 * 4)
    (['*', '+'], [2, 3, 4], 10), # (2 * 3) + 4
    
    # Operator precedence: Exponentiation before others
    (['+', '**'], [2, 3, 2], 11), # 2 + (3 ** 2)
    (['**', '+'], [2, 3, 2], 10), # (2 ** 3) + 2
    (['*', '**'], [2, 3, 2], 18), # 2 * (3 ** 2)
    
    # Floor division and subtraction
    (['//', '-'], [10, 2, 1], 4), # (10 // 2) - 1
    (['-', '//'], [10, 4, 2], 8), # 10 - (4 // 2)
    
    # Complex mixed operations
    (['+', '*', '//', '**'], [1, 2, 3, 4, 2], 11), # 1 + (2 * 3) // (4 ** 2) -> 1 + 6 // 16 -> 1 + 0 = 1
    # Wait, let's re-calc: 1 + 2 * 3 // 4**2 = 1 + 6 // 16 = 1 + 0 = 1.
    # Let's try a different one:
    (['*', '+', '**'], [2, 3, 4, 2], 22), # (2 * 3) + (4 ** 2) = 6 + 16 = 22
    
    # Edge cases: Zeroes
    (['+'], [0, 0], 0),
    (['*'], [0, 10], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    
    # Large numbers
    (['**', '*'], [2, 10, 2], 2048), # (2**10) * 2 = 1024 * 2
])
def test_do_algebra_success(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_large_exponent():
    # Testing that it handles reasonably large results
    assert do_algebra(['**'], [2, 64]) == 18446744073709551616