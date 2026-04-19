
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
    # Example case
    (['+', '*', '-'], [2, 3, 4, 5], 9), 
    # Simple operations
    (['+'], [10, 20], 30),
    (['-'], [10, 20], -10),
    (['*'], [5, 6], 30),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    # Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),  # 2 + (3 * 4) = 14
    (['*', '+'], [2, 3, 4], 10),  # (2 * 3) + 4 = 10
    (['-', '//'], [20, 10, 3], 17), # 20 - (10 // 3) = 17
    (['-', '*'], [10, 2, 3], 4),  # 10 - (2 * 3) = 4
    (['*', '-'], [10, 2, 3], 17), # (10 * 2) - 3 = 17
    (['-', '//'], [10, 4, 2], 8), # 10 - (4 // 2) = 8
    # Precedence: Exponentiation first
    (['+', '**'], [2, 3, 2], 11),   # 2 + (3 ** 2) = 11
    (['**', '+'], [2, 3, 2], 10),   # (2 ** 3) + 2 = 10
    (['*', '**'], [2, 3, 2], 18),   # 2 * (3 ** 2) = 18
    (['**', '*'], [2, 3, 2], 16),   # (2 ** 3) * 2 = 16
    # Associativity: Exponentiation is right-associative in Python
    (['**', '**'], [2, 3, 2], 512), # 2 ** (3 ** 2) = 2 ** 9 = 512
    # Complex mixtures
    (['+', '*', '//', '-'], [1, 2, 8, 2, 5], 4), # 1 + (2 * 8 // 2) - 5 = 4
    (['+', '**', '*'], [2, 3, 2, 4], 38),       # 2 + (3**2 * 4) = 38
    (['//', '+'], [10, 3, 2], 5), # (10 // 3) + 2 = 5
    (['**', '*', '//', '+'], [2, 3, 4, 2, 5], 21), # (2**3 * 4 // 2) + 5 = 21
    (['+', '*', '//'], [10, 2, 5, 2], 15), # 10 + (2 * 5 // 2) = 15
    (['+', '-', '*', '//', '**'], [10, 2, 3, 4, 2, 2], 9), # 10 + 2 - (3 * 4 // 2**2) = 9
    # Large numbers
    (['**', '+'], [10, 5, 100], 100100),
    (['**', '+'], [2, 10, 5], 1029),
    # Zeros and Negatives
    (['*'], [0, 100], 0),
    (['+'], [0, 0], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    (['*', '+'], [0, 5, 10], 10),
    (['+', '*'], [5, 0, 10], 5),
    (['-'], [1, 10], -9),
    (['//'], [0, 5], 0),
])
def test_do_algebra_parametrized(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_minimum_input():
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['-'], [1, 1]) == 0

def test_do_algebra_floor_division_behavior():
    # Ensure it is floor division, not float division
    assert do_algebra(['//'], [7, 2]) == 3
    assert do_algebra(['//'], [10, 3]) == 3

def test_do_algebra_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000
    assert do_algebra(['**'], [10, 5]) == 100000

def test_do_algebra_large_chain():
    # Testing a longer sequence of the same operator
    operators = ['+'] * 4
    operands = [1, 2, 3, 4, 5]
    assert do_algebra(operators, operands) == 15