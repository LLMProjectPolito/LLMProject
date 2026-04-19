
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
    
    # Mixed operations with precedence (PEMDAS)
    (['+', '*', '-'], [2, 3, 4, 5], 9),  # 2 + (3 * 4) - 5 = 9
    (['+', '**'], [2, 3, 2], 11),        # 2 + (3 ** 2) = 11
    (['*', '//'], [10, 2, 5], 4),        # (10 * 2) // 5 = 4
    (['**', '+', '*'], [2, 3, 4, 2], 16), # (2 ** 3) + (4 * 2) = 8 + 8 = 16
    
    # Edge cases: Minimum size
    (['+'], [0, 0], 0),
    (['-'], [0, 10], -10),
    (['*'], [0, 10], 0),
    (['**'], [10, 0], 1),
    
    # Complex precedence and floor division
    (['+', '//', '*'], [10, 3, 2, 4], 13), # 10 + (3 // 2 * 4) = 10 + (1 * 4) = 14? 
                                           # Wait: 3 // 2 = 1; 1 * 4 = 4; 10 + 4 = 14.
                                           # Let's re-verify: 10 + (3 // 2) * 4 = 10 + 1 * 4 = 14.
    (['-', '**', '//'], [20, 2, 3, 2], 11), # 20 - (2 ** 3) // 2 = 20 - 8 // 2 = 20 - 4 = 16.
                                            # Let's re-calculate: 20 - (8 // 2) = 16.
    
    # Large numbers
    (['**', '+'], [2, 10, 100], 1124), # 2**10 + 100 = 1024 + 100 = 1124,
])
def test_do_algebra_parametrized(operators, operands, expected):
    # Note: The logic for the complex cases above is based on Python's eval() behavior
    # which the function is expected to mimic.
    # Re-calculating the complex ones for the test cases:
    # ['+', '//', '*'], [10, 3, 2, 4] -> 10 + (3 // 2) * 4 = 10 + 1 * 4 = 14
    # ['-', '**', '//'], [20, 2, 3, 2] -> 20 - (2**3 // 2) = 20 - 4 = 16
    pass

# Correcting the parametrized values based on Python evaluation rules
@pytest.mark.parametrize("operators, operands, expected", [
    (['+'], [1, 2], 3),
    (['-'], [5, 2], 3),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['+', '**'], [2, 3, 2], 11),
    (['*', '//'], [10, 2, 5], 4),
    (['**', '+', '*'], [2, 3, 4, 2], 16),
    (['+'], [0, 0], 0),
    (['-'], [0, 10], -10),
    (['*'], [0, 10], 0),
    (['**'], [10, 0], 1),
    (['+', '//', '*'], [10, 3, 2, 4], 14),
    (['-', '**', '//'], [20, 2, 3, 2], 16),
    (['**', '+'], [2, 10, 100], 1124),
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_long_expression():
    operators = ['+', '-', '*', '//', '**']
    operands = [1, 2, 3, 4, 5, 2]
    # Expression: 1 + 2 - 3 * 4 // 5 ** 2
    # 5 ** 2 = 25
    # 3 * 4 = 12
    # 12 // 25 = 0
    # 1 + 2 - 0 = 3
    assert do_algebra(operators, operands) == 3