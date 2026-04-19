
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
    (['-'], [5, 2], 3),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Example case from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    
    # Order of operations: Exponentiation first
    (['+', '**'], [2, 3, 2], 11), # 2 + (3**2) = 11
    (['**', '+'], [2, 3, 4], 12), # (2**3) + 4 = 12
    
    # Order of operations: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14), # 2 + (3*4) = 14
    (['*', '+'], [2, 3, 4], 10), # (2*3) + 4 = 10
    (['-', '//'], [10, 5, 2], 8), # 10 - (5//2) = 10 - 2 = 8
    (['//', '-'], [10, 5, 2], 0), # (10//5) - 2 = 2 - 2 = 0
    
    # Complex mixed operations
    (['*', '//', '+'], [10, 2, 5, 3], 7), # (10 * 2 // 5) + 3 = 4 + 3 = 7
    (['**', '*', '//'], [2, 3, 2, 4], 3), # (2**3 * 2) // 4 = 16 // 4 = 4 -> Wait: 2**3=8, 8*2=16, 16//4=4
    (['**', '*', '//'], [2, 3, 2, 4], 4), 
    
    # Large numbers and zeros
    (['+'], [0, 0], 0),
    (['*'], [0, 100], 0),
    (['**'], [10, 0], 1),
    (['**'], [0, 10], 0),
    (['+'], [1000, 2000], 3000),
    
    # Long sequences
    (['+', '+', '+', '+'], [1, 1, 1, 1, 1], 5),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_floor_division_precision():
    # Ensure floor division is used, not float division
    assert do_algebra(['//'], [7, 2]) == 3

def test_do_algebra_exponentiation_priority():
    # 2 * 3 ** 2 should be 2 * 9 = 18, not 6 ** 2 = 36
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18