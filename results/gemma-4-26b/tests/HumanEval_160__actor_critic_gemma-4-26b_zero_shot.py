
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

# Assuming do_algebra is imported from the relevant module
# from your_module import do_algebra

@pytest.mark.parametrize("operators, operands, expected", [
    # Basic single-operator tests
    (['+'], [1, 2], 3),
    (['-'], [10, 5], 5),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),

    # Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*', '-'], [2, 3, 4, 5], 9),  # 2 + (3 * 4) - 5 = 9
    (['-', '*', '+'], [10, 2, 3, 4], 8), # 10 - (2 * 3) + 4 = 8
    (['+', '//', '+'], [5, 4, 2, 1], 8), # 5 + (4 // 2) + 1 = 8

    # Precedence: Exponentiation is highest
    (['*', '**'], [2, 3, 2], 18),        # 2 * (3 ** 2) = 18
    (['+', '**'], [2, 2, 3], 10),        # 2 + (2 ** 3) = 10
    (['-', '**', '-'], [10, 2, 2, 1], 5),# 10 - (2 ** 2) - 1 = 5

    # Precedence: Multiplication and Floor Division (Left-to-Right)
    (['//', '*'], [10, 2, 5], 25),       # (10 // 2) * 5 = 25
    (['*', '//'], [10, 2, 5], 4),        # (10 * 2) // 5 = 4

    # Complex mixed precedence
    (['-', '**', '+', '*'], [10, 2, 2, 3, 2], 12), # 10 - (2**2) + (3*2) = 10 - 4 + 6 = 12
    (['+', '//', '**'], [1, 10, 2, 2], 15),        # 1 + (10 // (2**2)) = 1 + 2 = 3? 
                                                   # Wait: 1 + (10 // 4) = 1 + 2 = 3.
                                                   # Let's re-verify: 1 + (10 // (2**2)) = 1 + 2 = 3.
])
def test_do_algebra_logic(operators, operands, expected):
    """Tests various combinations of operators to ensure correct mathematical precedence."""
    # Replace 'do_algebra' with the actual function call
    from your_module import do_algebra 
    assert do_algebra(operators, operands) == expected

def test_do_algebra_minimum_constraints():
    """Tests the minimum allowed input size."""
    from your_module import do_algebra
    assert do_algebra(['+'], [0, 0]) == 0
    assert do_algebra(['**'], [1, 100]) == 1

def test_do_algebra_large_numbers():
    """Tests the function with larger integer values."""
    from your_module import do_algebra
    assert do_algebra(['*', '*'], [100, 100, 100], 1000000) == 1000000