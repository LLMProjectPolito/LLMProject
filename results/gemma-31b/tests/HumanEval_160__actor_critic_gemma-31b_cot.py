
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
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 5], 2),
    (['**'], [2, 3], 8),
    # Multiple operations of same type
    (['+', '+', '+'], [1, 1, 1, 1], 4),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    # Negative numbers
    (['-'], [-10, -5], -5),      # -10 - (-5) = -5
    (['+'], [-10, 5], -5),       # -10 + 5 = -5
    (['*'], [-2, -3], 6),        # -2 * -3 = 6
    (['**'], [-2, 2], 4),        # (-2)**2 = 4
    (['**'], [-2, 3], -8),       # (-2)**3 = -8
    # Floating point precision
    (['+'], [1.1, 2.2], pytest.approx(3.3)),
    (['*'], [0.1, 0.2], pytest.approx(0.02)),
    (['-'], [5.5, 2.1], pytest.approx(3.4)),
    # Negative Exponents (Critical edge case)
    (['**'], [2, -1], 0.5),      # 2**-1 = 0.5
    (['**'], [4, -0.5], 0.5),    # 4**-0.5 = 1/sqrt(4) = 0.5
])
def test_do_algebra_parametrized(operators, operands, expected):
    """Merged test for basic operations, negatives, floats, and negative exponents."""
    assert do_algebra(operators, operands) == expected

def test_do_algebra_precedence():
    """Test that Python's operator precedence (PEMDAS) is respected."""
    # 2 + (3 * 4) - 5 = 2 + 12 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    
    # 2 + (3 ** 2) * 4 = 2 + 9 * 4 = 2 + 36 = 38
    assert do_algebra(['+', '**', '*'], [2, 3, 2, 4]) == 38
    
    # (2 ** 3) + (4 * 2) = 8 + 8 = 16
    assert do_algebra(['**', '+', '*'], [2, 3, 4, 2]) == 16
    
    # 10 * 2 + 5 // 3 = 20 + 1 = 21
    assert do_algebra(['*', '+', '//'], [10, 2, 5, 3]) == 21

def test_do_algebra_right_associativity_exponent():
    """Test that exponentiation is right-associative in Python (2**3**2 is 2**9)."""
    # 2 ** (3 ** 2) = 2 ** 9 = 512
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512

def test_do_algebra_edge_cases():
    """Test edge cases including zeros and large numbers."""
    # Minimum length constraints
    assert do_algebra(['+'], [0, 0]) == 0
    
    # Exponentiation with zero
    assert do_algebra(['**'], [5, 0]) == 1
    assert do_algebra(['**'], [0, 5]) == 0
    assert do_algebra(['**'], [0, 0]) == 1  # 0**0 is 1 in Python
    
    # Floor division resulting in zero
    assert do_algebra(['//'], [1, 2]) == 0
    
    # Large numbers
    assert do_algebra(['**', '*'], [2, 10, 2]) == 2048 # (2**10) * 2

def test_do_algebra_complex_expression():
    """Test a longer expression with mixed operators."""
    # 1 + 2 - 3 * 4 // 5 ** 2
    # 5**2 = 25
    # 3 * 4 // 25 = 12 // 25 = 0
    # 1 + 2 - 0 = 3
    assert do_algebra(['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2]) == 3

def test_do_algebra_division_by_zero():
    """Test that division by zero raises the appropriate error."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])
    
    with pytest.raises(ZeroDivisionError):
        do_algebra(['+', '//'], [5, 10, 0])

def test_do_algebra_invalid_inputs():
    """Test mismatched lengths, empty/single inputs, and unsupported operators."""
    # Mismatched Input Lengths
    with pytest.raises(ValueError):
        do_algebra(['+'], [1]) # Too few operands
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3]) # Too many operands
    
    # Empty or Single-Value Inputs
    with pytest.raises(ValueError):
        do_algebra([], [5]) # No operators
    with pytest.raises(ValueError):
        do_algebra([], []) # Empty lists
    
    # Invalid Operators (Including True Division '/' as explicitly unsupported)
    with pytest.raises(ValueError):
        do_algebra(['/'], [10, 2])
    with pytest.raises(ValueError):
        do_algebra(['%'], [10, 3])
    with pytest.raises(ValueError):
        do_algebra(['&'], [10, 3])
    with pytest.raises(ValueError):
        do_algebra(['+', '?'], [1, 2, 3])

def test_do_algebra_type_validation():
    """Test that the function handles non-list inputs and non-numeric operands."""
    # Non-list inputs for operators or operands
    with pytest.raises(TypeError):
        do_algebra("+", [1, 2])
    with pytest.raises(TypeError):
        do_algebra(['+'], 10)
    with pytest.raises(TypeError):
        do_algebra(None, [1, 2])
    with pytest.raises(TypeError):
        do_algebra(['+'], None)

    # Non-numeric operands
    with pytest.raises(TypeError):
        do_algebra(['+'], [1, "2"])
    with pytest.raises(TypeError):
        do_algebra(['*'], [None, 5])
    with pytest.raises(TypeError):
        do_algebra(['-'], [[1], 2])

def test_do_algebra_overflow():
    """Test for extremely large exponents that trigger OverflowError."""
    # Using floats to trigger OverflowError rather than MemoryError from huge ints
    with pytest.raises(OverflowError):
        do_algebra(['**'], [10.0, 1000.0])