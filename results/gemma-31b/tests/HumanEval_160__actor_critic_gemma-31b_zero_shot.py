
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
    """
    # Construct the expression string by interleaving operands and operators
    expression = ""
    for i in range(len(operator)):
        expression += str(operand[i]) + operator[i]
    expression += str(operand[-1])
    
    # eval() follows standard Python operator precedence (PEMDAS)
    return eval(expression)

@pytest.mark.parametrize("operators, operands, expected", [
    # Basic Example from problem description
    (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + (3 * 4) - 5 = 2 + 12 - 5 = 9
    
    # Minimum constraints: 1 operator, 2 operands
    (['+'], [1, 2], 3),
    (['-'], [10, 5], 5),
    (['*'], [4, 3], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Operator Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [1, 2, 3], 7),       # 1 + (2 * 3) = 7
    (['*', '+'], [1, 2, 3], 5),       # (1 * 2) + 3 = 5
    (['-', '*'], [10, 2, 3], 4),      # 10 - (2 * 3) = 4
    (['+', '//'], [10, 10, 3], 13),   # 10 + (10 // 3) = 10 + 3 = 13
    
    # Operator Precedence: Exponentiation is highest
    (['+', '**'], [2, 3, 2], 11),     # 2 + (3 ** 2) = 2 + 9 = 11
    (['**', '*'], [2, 3, 2], 16),     # (2 ** 3) * 2 = 8 * 2 = 16
    (['**', '+'], [2, 3, 4], 12),     # (2 ** 3) + 4 = 8 + 4 = 12
    
    # Complex mixed expression
    (['**', '*', '//', '+'], [2, 3, 4, 5, 6], 12), 
    # (2**3) * 4 // 5 + 6 => 8 * 4 // 5 + 6 => 32 // 5 + 6 => 6 + 6 = 12
    
    # Edge Case: Zeroes
    (['*', '+'], [0, 5, 10], 10),     # 0 * 5 + 10 = 10
    (['+', '*'], [0, 5, 0], 0),       # 0 + 5 * 0 = 0
    (['**'], [0, 5], 0),              # 0 ** 5 = 0
    (['**'], [5, 0], 1),              # 5 ** 0 = 1
    
    # Edge Case: Negative results (operands are non-negative, but result can be negative)
    (['-'], [5, 10], -5),             # 5 - 10 = -5
    (['-', '-'], [10, 20, 30], -40),  # 10 - 20 - 30 = -40
    
    # Edge Case: Large numbers
    (['**', '+'], [2, 10, 1], 1025),  # 2**10 + 1 = 1024 + 1 = 1025
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_invalid_input():
    """
    Optional: Test how the function handles cases that violate the problem constraints
    if validation were implemented. Currently, it relies on eval().
    """
    # This is just to ensure the function doesn't crash on basic valid types
    # but the problem statement guarantees the constraints.
    assert do_algebra(['+'], [1, 1]) == 2