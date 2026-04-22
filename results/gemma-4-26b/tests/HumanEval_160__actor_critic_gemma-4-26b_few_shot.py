
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

# Note: The implementation of do_algebra is assumed to be available in the scope.

def test_do_algebra_single_operator():
    """Tests the simplest case with one operator and two operands."""
    assert do_algebra(['+'], [10, 5]) == 15
    assert do_algebra(['-'], [10, 5]) == 5
    assert do_algebra(['*'], [10, 5]) == 50
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_precedence():
    """Tests that standard mathematical operator precedence (PEMDAS) is respected."""
    # Multiplication before Addition: 2 + (3 * 4) = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14
    
    # Exponentiation before Multiplication: 2 * 3 ** 2 = 2 * 9 = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    
    # Floor division before Subtraction: 10 - 6 // 3 = 10 - 2 = 8
    assert do_algebra(['-', '//'], [10, 6, 3]) == 8

    # Exponentiation Associativity: Python's ** is right-associative
    # 2 ** (3 ** 2) = 2 ** 9 = 512
    # (Incorrect left-associative evaluation would be (2**3)**2 = 64)
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512

def test_do_algebra_complex_chain():
    """Tests a longer chain of various operators."""
    # 2 ** 3 // 4 + 5 * 2
    # (2**3) // 4 + (5 * 2) -> 8 // 4 + 10 -> 2 + 10 = 12
    assert do_algebra(['**', '//', '+', '*'], [2, 3, 4, 5, 2]) == 12

def test_do_algebra_negative_numbers():
    """Tests that the function handles negative operands correctly."""
    # -5 - (-10) + 5 = 5 + 5 = 10
    assert do_algebra(['-', '+'], [-5, -10, 5]) == 10
    # -2 * 3 = -6
    assert do_algebra(['*'], [-2, 3]) == -6

@pytest.mark.parametrize("operators, operands, expected", [
    (['+', '+'], [1, 1, 1], 3),
    (['-', '-'], [10, 5, 2], 3),
    (['+', '-'], [10, 5, 5], 10),
    (['**', '**'], [2, 2, 3], 256), 
])
def test_do_algebra_parametrized(operators, operands, expected):
    """Parametrized test for various combinations without conditional logic."""
    assert do_algebra(operators, operands) == expected

def test_do_algebra_zero_handling():
    """Tests edge cases involving zero."""
    # Zero as an operand
    assert do_algebra(['+', '*'], [0, 5, 2]) == 10
    assert do_algebra(['-', '*'], [5, 0, 5]) == 5
    # Exponentiation with zero
    assert do_algebra(['**'], [5, 0]) == 1
    assert do_algebra(['**'], [0, 0]) == 1  # 0 ** 0 is 1 in Python
    
    # Zero division via exponentiation
    with pytest.raises(ZeroDivisionError):
        do_algebra(['**'], [0, -1])

def test_do_algebra_floating_point():
    """Tests floating point division and negative exponents."""
    # Standard division
    assert do_algebra(['/'], [5, 2]) == 2.5
    # Negative exponent resulting in float
    assert do_algebra(['**'], [2, -1]) == 0.5

def test_do_algebra_division_by_zero():
    """Verifies that division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])
    with pytest.raises(ZeroDivisionError):
        do_algebra(['/'], [10, 0])

def test_do_algebra_invalid_inputs():
    """Tests for various invalid input scenarios."""
    
    # Mismatched lengths: Too few operators
    with pytest.raises(ValueError):
        do_algebra(['+', '*'], [1, 2])
        
    # Mismatched lengths: Too many operands
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3])
        
    # Single operand (Docstring requires at least one operator and two operands)
    with pytest.raises(ValueError):
        do_algebra([], [5])

    # Empty lists
    with pytest.raises(ValueError):
        do_algebra([], [])
    
    # Unsupported operators
    with pytest.raises(ValueError):
        do_algebra(['%'], [10, 2])
    
    # Non-numeric inputs
    with pytest.raises(TypeError):
        do_algebra(['+'], [1, 'a'])
    
    with pytest.raises(TypeError):
        do_algebra(['+'], ['a', 'b'])

def test_do_algebra_large_numbers():
    """Tests the function with large integers."""
    assert do_algebra(['*', '*'], [100, 100, 100]) == 1000000