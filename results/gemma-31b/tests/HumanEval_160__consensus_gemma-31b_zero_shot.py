
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
    
    # Example from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9), # 2 + (3 * 4) - 5 = 9
    
    # Operator Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [1, 2, 3], 7),       # 1 + (2 * 3) = 7
    (['*', '+'], [1, 2, 3], 5),       # (1 * 2) + 3 = 5
    (['-', '//'], [10, 4, 2], 8),     # 10 - (4 // 2) = 8
    (['//', '-'], [10, 4, 2], 0),     # (10 // 4) - 2 = 0
    (['+', '*'], [2, 3, 4], 14),      # 2 + (3 * 4) = 14
    (['*', '+'], [2, 3, 4], 10),      # (2 * 3) + 4 = 10
    (['-', '//'], [10, 5, 2], 8),     # 10 - (5 // 2) = 8
    (['//', '-'], [10, 5, 2], 0),     # (10 // 5) - 2 = 0
    
    # Operator Precedence: Exponentiation highest
    (['+', '**'], [2, 3, 2], 11),     # 2 + (3 ** 2) = 11
    (['**', '+'], [2, 3, 4], 12),     # (2 ** 3) + 4 = 12
    (['*', '**'], [2, 3, 2], 18),     # 2 * (3 ** 2) = 18
    (['**', '*'], [2, 3, 2], 16),     # (2 ** 3) * 2 = 16
    (['**', '//'], [10, 2, 3], 33),   # (10 ** 2) // 3 = 33
    (['**', '**'], [2, 3, 2], 512),   # 2 ** (3 ** 2) = 512 (Right-associativity)
    
    # Complex mixed precedence
    (['+', '*', '//', '**'], [1, 2, 3, 4, 2], 1), # 1 + (2 * 3 // 16) = 1 + 0 = 1
    (['**', '+', '*'], [2, 2, 3, 4], 16),        # (2 ** 2) + (3 * 4) = 16
    (['-', '*', '**'], [20, 2, 3, 2], 2),        # 20 - (2 * 9) = 2
    (['+', '*', '**', '//'], [1, 2, 3, 2, 4], 5), # 1 + (2 * 9 // 4) = 1 + 4 = 5
    (['+', '*', '**'], [2, 3, 4, 2], 50),        # 2 + (3 * 16) = 50
    
    # Edge cases: Zeroes
    (['+'], [0, 0], 0),
    (['*'], [0, 10], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    (['//'], [0, 5], 0),
    (['-'], [0, 5], -5),
    (['*', '+'], [0, 10, 5], 5),
    (['+', '*'], [5, 0, 10], 5),
    
    # Large numbers
    (['**'], [10, 5], 100000),
    (['*'], [1000, 1000], 1000000),
    (['**', '+'], [2, 10, 100], 1124), # 1024 + 100
    (['+', '*'], [100, 200, 300], 60100), # 100 + 60000
    (['**'], [10, 6], 1000000),
])
def test_do_algebra_parametrized(operators, operands, expected):
    """Tests various combinations of operators and operands to ensure correct evaluation and precedence."""
    assert do_algebra(operators, operands) == expected

def test_do_algebra_minimal_input():
    """Tests the minimum required input size (1 operator, 2 operands)."""
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['-'], [1, 1]) == 0
    assert do_algebra(['+'], [10, 5]) == 15
    assert do_algebra(['-'], [10, 5]) == 5
    assert do_algebra(['*'], [10, 5]) == 50

def test_do_algebra_long_chain():
    """Tests a longer sequence of operations."""
    # 1 + 1 + 1 + 1 + 1
    assert do_algebra(['+', '+', '+', '+'], [1, 1, 1, 1, 1]) == 5
    # 2 * 2 * 2 * 2 * 2
    assert do_algebra(['*', '*', '*', '*'], [2, 2, 2, 2, 2]) == 32

def test_do_algebra_floor_division_behavior():
    """Ensures floor division is used specifically."""
    assert do_algebra(['//'], [7, 2]) == 3
    assert do_algebra(['//'], [1, 2]) == 0
    assert do_algebra(['//', '+'], [15, 4, 2]) == 5 # (15 // 4) + 2 = 3 + 2 = 5