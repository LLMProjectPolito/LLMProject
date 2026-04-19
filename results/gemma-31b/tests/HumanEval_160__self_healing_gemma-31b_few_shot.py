
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
    expression = str(operand[0])
    for op, val in zip(operator, operand[1:]):
        expression += f" {op} {val}"
    return eval(expression)

@pytest.mark.parametrize("operators, operands, expected", [
    # Basic single operations
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),  # 2 + (3 * 4)
    (['*', '+'], [2, 3, 4], 10),  # (2 * 3) + 4
    (['-', '//'], [10, 4, 2], 8), # 10 - (4 // 2) = 10 - 2
    (['//', '-'], [10, 4, 2], 0), # (10 // 4) - 2 = 2 - 2
    
    # Precedence: Exponentiation before others
    (['+', '**'], [2, 3, 2], 11), # 2 + (3 ** 2) = 2 + 9
    (['**', '+'], [2, 3, 2], 10), # (2 ** 3) + 2 = 8 + 2
    (['*', '**'], [2, 3, 2], 18), # 2 * (3 ** 2) = 2 * 9
    
    # Example from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
    
    # Complex mixed operations
    (['**', '*', '//', '+'], [2, 3, 2, 10, 5], 6), # (2**3 * 2 // 10) + 5 = (8 * 2 // 10) + 5 = 1 + 5 = 6
    (['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2], 3), # 1 + 2 - 3 * 4 // 5 ** 2 = 1 + 2 - 12 // 25 = 3 - 0 = 3
    (['+', '*', '**'], [2, 3, 2, 2], 14), # 2 + 3 * 2**2 = 2 + 3 * 4 = 14
    
    # Edge cases: zeros and negative results
    (['*'], [0, 100], 0),
    (['-'], [5, 10], -5),
    (['+'], [0, 0], 0),
    (['**'], [5, 0], 1),
    (['//'], [0, 5], 0),
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_large_numbers():
    # Test with larger integers
    operators = ['*', '**']
    operands = [100, 2, 3]
    # 100 * (2**3) = 800
    assert do_algebra(operators, operands) == 800

def test_do_algebra_minimum_length():
    # Minimum length: 1 operator, 2 operands
    assert do_algebra(['+'], [1, 1]) == 2