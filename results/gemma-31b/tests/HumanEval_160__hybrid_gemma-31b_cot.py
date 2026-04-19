
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
    # --- Basic Operations (Single Operator) ---
    (['+'], [10, 20], 30),
    (['-'], [20, 10], 10),
    (['-'], [10, 20], -10),
    (['*'], [5, 6], 30),
    (['//'], [10, 3], 3),
    (['//'], [20, 5], 4),
    (['**'], [2, 3], 8),
    (['**'], [3, 2], 9),
    (['**'], [5, 0], 1),
    (['+'], [1, 1], 2),
    (['-'], [1, 1], 0),

    # --- Operator Precedence: PEMDAS ---
    # Multiplication/Division before Addition/Subtraction
    (['+', '*', '-'], [2, 3, 4, 5], 9),   # 2 + (3 * 4) - 5 = 9
    (['+', '*'], [2, 3, 4], 14),          # 2 + (3 * 4) = 14
    (['*', '+'], [2, 3, 4], 10),          # (2 * 3) + 4 = 10
    (['-', '//'], [10, 4, 2], 8),         # 10 - (4 // 2) = 8
    (['//', '-'], [11, 4, 2], 0),         # (11 // 4) - 2 = 2 - 2 = 0
    (['//', '-'], [10, 4, 2], 0),         # (10 // 4) - 2 = 2 - 2 = 0
    (['+', '//', '*'], [10, 15, 3, 2], 20), # 10 + (15 // 3 * 2) = 10 + 10 = 20

    # Exponentiation before Multiplication/Division
    (['*', '**'], [2, 3, 2], 18),         # 2 * (3 ** 2) = 18
    (['**', '*'], [2, 3, 2], 16),         # (2 ** 3) * 2 = 16
    (['//', '**'], [100, 2, 3], 12),      # 100 // (2 ** 3) = 12
    (['**', '//'], [2, 3, 4], 2),         # (2 ** 3) // 4 = 2
    (['**', '+', '//'], [2, 3, 10, 2], 13), # (2 ** 3) + (10 // 2) = 13

    # Complex Mixed Expressions
    # 1 + (2 * (3 ** 4) // 2) = 1 + (2 * 81 // 2) = 1 + 81 = 82
    (['+', '*', '**', '//'], [1, 2, 3, 4, 2], 82),
    # 10 + 2 - (3 * 4 // (2 ** 2)) = 12 - (12 // 4) = 12 - 3 = 9
    (['+', '-', '*', '//', '**'], [10, 2, 3, 4, 2, 2], 9),

    # --- Edge Cases: Zeros and Minimal Inputs ---
    (['+', '*'], [0, 0, 0], 0),
    (['*', '**'], [0, 5, 2], 0),          # 0 * (5**2) = 0
    (['**', '+'], [0, 5, 2], 2),          # (0**5) + 2 = 2
    (['*', '+'], [0, 10, 0], 0),          # (0 * 10) + 0 = 0
    (['+', '//'], [10, 0, 5], 10),        # 10 + (0 // 5) = 10
    (['+'], [1, 2], 3),                   # Minimal input

    # --- Long Chains (Associativity) ---
    (['+', '+', '+'], [1, 1, 1, 1], 4),
    (['-', '-', '-'], [10, 1, 1, 1], 7),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    (['**', '**'], [2, 2, 2], 16),        # 2**(2**2) = 2**4 = 16
    (['//', '//'], [64, 4, 2], 8),        # (64 // 4) // 2 = 8
    (['//', '//'], [100, 5, 2], 10),      # (100 // 5) // 2 = 10

    # --- Large Numbers (Arbitrary Precision) ---
    (['*', '+'], [1000, 1000, 1000], 1001000),
    (['*', '**'], [10, 2, 10], 10240),    # 10 * (2**10) = 10240
])
def test_do_algebra_scenarios(operators, operands, expected):
    """Comprehensive test covering basic arithmetic, precedence, and edge cases."""
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    """Test that floor division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_complex_division_by_zero():
    """Test division by zero within a more complex expression."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['+', '//'], [5, 10, 0])