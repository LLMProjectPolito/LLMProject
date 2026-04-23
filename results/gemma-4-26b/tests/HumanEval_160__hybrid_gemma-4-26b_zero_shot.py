
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
    Given two lists: operator (basic algebra operations) and operand (integers).
    Builds the algebraic expression and returns the evaluation.
    """
    expression = str(operand[0])
    for op, val in zip(operator, operand[1:]):
        expression += f" {op} {val}"
    return eval(expression)

@pytest.mark.parametrize("operators, operands, expected", [
    # --- Basic Single Operations ---
    (['+'], [1, 2], 3),
    (['-'], [10, 5], 5),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    (['*'], [5, 0], 0),
    (['+'], [0, 0], 0),
    (['//'], [1, 10], 0),

    # --- Operator Precedence (PEMDAS/BODMAS) ---
    # Multiplication/Division vs Addition/Subtraction
    (['*', '+'], [2, 3, 4], 10),      # 2 + (3 * 4)
    (['+', '*'], [2, 3, 4], 14),      # (2 + 3) * 4 is wrong; 2 + (3 * 4) = 14
    (['-', '//'], [10, 4, 2], 8),     # 10 - (4 // 2)
    (['//', '-'], [10, 2, 4], 1),     # (10 // 2) - 4
    
    # Exponentiation vs Multiplication/Division
    (['*', '**'], [2, 3, 2], 18),     # 2 * (3 ** 2)
    (['**', '*'], [2, 3, 2], 16),     # (2 ** 3) * 2
    (['-', '**'], [10, 2, 3], 2),     # 10 - (2 ** 3)
    (['**', '-'], [2, 3, 2], -7),     # 2 - (3 ** 2)
    
    # --- Left-to-Right Associativity (Same Precedence Level) ---
    (['-', '+'], [10, 5, 2], 7),      # (10 - 5) + 2
    (['+', '-'], [10, 5, 2], 13),     # (10 + 5) - 2
    (['//', '*'], [10, 2, 5], 25),    # (10 // 2) * 5
    (['*', '//'], [10, 2, 5], 4),     # (10 * 2) // 5

    # --- Complex Mixed Expressions (3+ Operators) ---
    (['+', '*', '-'], [2, 3, 4, 5], 9),      # 2 + 12 - 5
    (['*', '+', '-'], [2, 3, 4, 5], 5),      # 6 + 4 - 5
    (['+', '-', '*'], [1, 2, 3, 4], -9),     # 1 + 2 - 12
    (['**', '+', '*'], [2, 2, 3, 4], 16),    # 4 + 12
    (['+', '//', '**'], [10, 2, 2, 3], 10),  # 10 + (2 // 8)
    (['-', '//', '*'], [20, 5, 2, 3], 14),   # 20 - (2 * 3)
    (['//', '*', '+'], [10, 2, 5, 5], 30),   # 5 * 5 + 5
    (['*', '+', '//'], [2, 5, 4, 2], 12),    # 10 + 2

    # --- Large Operands & Edge Cases ---
    (['**'], [10, 5], 100000),            # Large result
    (['**', '-'], [2, 5, 10], 22),        # 32 - 10
    (['+', '*'], [100, 200, 2], 500),     # 100 + 400
])
def test_do_algebra_parametrized(operators, operands, expected):
    """Comprehensive test covering basic, precedence, associativity, and complex chains."""
    assert do_algebra(operators, operands) == expected

def test_do_algebra_exponentiation_right_associativity():
    """
    Ensures exponentiation follows right-to-left associativity 
    (Standard Python/Mathematical behavior: 2^(3^2)).
    """
    # 2 ** (3 ** 2) = 2 ** 9 = 512
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512

def test_do_algebra_large_exponent():
    """Test specifically for large exponentiation handling."""
    assert do_algebra(['**'], [2, 10]) == 1024

def test_do_algebra_minimum_requirements():
    """Tests the absolute minimum requirements."""
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['*'], [0, 5]) == 0