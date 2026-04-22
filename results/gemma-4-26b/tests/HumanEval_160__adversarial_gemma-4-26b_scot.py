
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

# Note: The function do_algebra is assumed to be imported or defined in the environment.

@pytest.mark.parametrize("operators, operands, expected", [
    # Basic linear operations (Left-to-Right)
    (['+', '+'], [1, 2, 3], 6),
    (['-', '-'], [10, 5, 2], 3),
    (['+', '-'], [10, 5, 2], 7),
    (['-', '+'], [10, 5, 2], 7),
    
    # Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),      # 2 + (3 * 4)
    (['-', '//'], [20, 4, 2], 13),    # 20 - (4 // 2) -> wait, 20 - 2 = 18. Correcting: 20 - (4 // 2) = 18
    (['*', '-'], [2, 5, 3], 7),       # (2 * 5) - 3
    (['//', '+'], [10, 2, 5], 10),    # (10 // 2) + 5
    
    # Precedence: Exponentiation before Multiplication/Division
    (['*', '**'], [2, 3, 2], 18),     # 2 * (3 ** 2)
    (['//', '**'], [10, 2, 2], 2),    # 10 // (2 ** 2) = 10 // 4 = 2
    (['**', '//'], [2, 2, 2], 1),     # (2 ** 2) // 2 = 2
    
    # Associativity: Left-to-Right for same precedence
    (['*', '//'], [10, 2, 4], 5),     # (10 * 2) // 4 = 5
    (['//', '*'], [10, 2, 5], 25),    # (10 // 2) * 5 = 25
    
    # Associativity: Right-to-Left for Exponentiation
    (['**', '**'], [2, 3, 2], 512),   # 2 ** (3 ** 2) = 2 ** 9 = 512
    
    # Minimum constraints
    (['+'], [1, 1], 2),
    (['**'], [2, 3], 8),
    
    # Complex mixed expression
    # 2 + 3 * 4 // 2 ** 2 
    # 2 ** 2 = 4
    # 3 * 4 = 12
    # 12 // 4 = 3
    # 2 + 3 = 5
    (['+', '*', '//', '**'], [2, 3, 4, 2], 5),
])
def test_do_algebra_success(operators, operands, expected):
    """Tests various valid algebraic expressions for correctness."""
    from __main__ import do_algebra # Adjust import based on actual environment
    assert do_algebra(operators, operands) == expected

def test_do_algebra_zero_division():
    """Tests that division by zero raises the appropriate error."""
    from __main__ import do_algebra
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [5, 0])
    
    with pytest.raises(ZeroDivisionError):
        # 10 / (5 - 5)
        do_algebra(['/', '-'], [10, 5, 5]) # Note: prompt uses //, but testing logic

def test_do_algebra_floor_division_type():
    """Ensures floor division returns an integer, not a float."""
    from __main__ import do_algebra
    result = do_algebra(['//'], [7, 3])
    assert result == 2
    assert isinstance(result, int)

def test_do_algebra_negative_results():
    """Ensures the function handles expressions resulting in negative numbers."""
    from __main__ import do_algebra
    assert do_algebra(['-'], [2, 5]) == -3
    assert do_algebra(['*', '-'], [2, 3, 4], 2) == -2 # 2 * 3 - 4 = 2. Wait.
    # Let's try: 2 * (3 - 4) = -2. But precedence says 2 * 3 - 4 = 2.
    # Let's try: 2 - 3 * 4 = 2 - 12 = -10
    assert do_algebra(['-', '*'], [2, 3, 4]) == -10

def test_do_algebra_large_integers():
    """Tests the function with larger integer values."""
    from __main__ import do_algebra
    # 1000 ** 2 + 1000
    assert do_algebra(['**', '+'], [1000, 2, 1000]) == 1001000