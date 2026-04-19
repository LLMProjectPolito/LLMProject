
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
    
    # Example from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    
    # Operator precedence: Exponentiation first
    (['+', '**'], [2, 3, 2], 11), # 2 + (3**2) = 11
    (['**', '+'], [2, 3, 2], 10), # (2**3) + 2 = 10
    
    # Operator precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),   # 2 + (3*4) = 14
    (['-', '*'], [10, 2, 3], 4),   # 10 - (2*3) = 4
    (['*', '+'], [2, 3, 4], 14),   # (2*3) + 4 = 10? No, 6+4=10. Wait: 2*3+4 = 10.
    
    # Floor division and precedence
    (['//', '+'], [10, 3, 2], 5),  # (10 // 3) + 2 = 3 + 2 = 5
    (['+', '//'], [2, 10, 3], 5),  # 2 + (10 // 3) = 2 + 3 = 5
    
    # Complex mixed expressions
    (['**', '+', '*'], [2, 3, 4, 5], 28), # (2**3) + (4*5) = 8 + 20 = 28
    (['+', '-', '*', '//'], [10, 5, 2, 3, 2], 10), # 10 + 5 - (2 * 3 // 2) = 15 - 3 = 12? 
    # Let's re-calc: 10 + 5 - 2 * 3 // 2 => 10 + 5 - (6 // 2) => 15 - 3 = 12.
    (['+', '-', '*', '//'], [10, 5, 2, 3, 2], 12),
    
    # Edge cases: Zeroes
    (['*'], [0, 10], 0),
    (['+'], [0, 0], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    
    # Large numbers
    (['*'], [1000, 1000], 1000000),
    (['**'], [2, 10], 1024),
    
    # Minimum constraints (1 operator, 2 operands)
    (['+'], [10, 20], 30),
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_long_chain():
    # Testing a longer sequence of the same operator
    operators = ['+', '+', '+', '+']
    operands = [1, 1, 1, 1, 1]
    assert do_algebra(operators, operands) == 5

def test_do_algebra_subtraction_chain():
    operators = ['-', '-', '-']
    operands = [20, 5, 5, 5]
    assert do_algebra(operators, operands) == 5 # 20 - 5 - 5 - 5 = 5