
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

def test_do_algebra_basic():
    """Test basic addition and subtraction."""
    assert do_algebra(['+', '-'], [10, 5, 2]) == 13  # 10 + 5 - 2 = 13
    assert do_algebra(['-'], [10, 3]) == 7           # 10 - 3 = 7

def test_do_algebra_precedence():
    """Test that standard operator precedence (PEMDAS) is followed."""
    # Multiplication before addition: 2 + (3 * 4) = 14
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14
    # Exponentiation before multiplication: 2 * (3 ** 2) = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    # Mixed: 2 + 3 * 4 - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_do_algebra_associativity():
    """
    Test associativity rules:
    - Exponentiation is right-associative.
    - Addition, Subtraction, Multiplication, and Division are left-associative.
    """
    # Right-associativity: 2**3**2 = 2**(3**2) = 512
    assert do_algebra(['**', '**'], [2, 3, 2]) == 512
    
    # Left-associativity: (10 - 5) + 2 = 7 (NOT 10 - (5 + 2) = 3)
    assert do_algebra(['-', '+'], [10, 5, 2]) == 7
    
    # Left-associativity: (10 * 2) / 5 = 4.0 (NOT 10 * (2 / 5) = 4.0, but logic differs)
    # Using floor division to be clear: (10 // 3) // 2 = 3 // 2 = 1
    assert do_algebra(['//', '//'], [10, 3, 2]) == 1

def test_do_algebra_division():
    """Test both true division (/) and floor division (//)."""
    # Floor division
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['+', '//'], [5, 10, 3]) == 8  # 5 + (10 // 3) = 8
    
    # True division
    assert do_algebra(['/'], [10, 4]) == 2.5
    assert do_algebra(['+', '/'], [1, 10, 4]) == 3.5 # 1 + 2.5 = 3.5

def test_do_algebra_exponentiation():
    """Test exponentiation including negative exponents."""
    assert do_algebra(['**'], [2, 3]) == 8
    assert do_algebra(['**', '+'], [2, 3, 1]) == 9   # (2 ** 3) + 1 = 9
    
    # Negative exponents: 2^-1 = 0.5
    assert do_algebra(['**'], [2, -1]) == 0.5
    assert do_algebra(['**'], [4, -2]) == 0.0625

def test_do_algebra_minimum_input():
    """Test the smallest possible valid input (1 operator, 2 operands)."""
    assert do_algebra(['+'], [1, 1]) == 2
    assert do_algebra(['*'], [0, 100]) == 0

def test_do_algebra_with_zeroes():
    """Test cases involving zero as an operand."""
    assert do_algebra(['*', '+'], [0, 5, 10]) == 10  # (0 * 5) + 10 = 10
    assert do_algebra(['**'], [5, 0]) == 1
    assert do_algebra(['**'], [0, 5]) == 0

def test_do_algebra_large_numbers():
    """Test with larger integers and potential overflow scenarios."""
    assert do_algebra(['*', '*'], [100, 100, 100]) == 1000000
    # Python handles arbitrarily large integers, but we test a large power
    assert do_algebra(['**'], [2, 100]) == 1267650600228229401496703205376

def test_do_algebra_negative_numbers():
    """Test that negative operands are handled correctly."""
    assert do_algebra(['+'], [-10, -5]) == -15
    assert do_algebra(['-'], [-10, -5]) == -5   # -10 - (-5) = -5
    assert do_algebra(['*'], [-2, 3]) == -6
    assert do_algebra(['**'], [-2, 3]) == -8    # (-2)^3 = -8

def test_do_algebra_floats():
    """Test with floating point numbers using pytest.approx for precision."""
    assert do_algebra(['+'], [0.1, 0.2]) == pytest.approx(0.3)
    assert do_algebra(['*'], [0.5, 0.2]) == pytest.approx(0.1)
    # Testing precision with division
    assert do_algebra(['/'], [1, 3]) == pytest.approx(0.3333333333333333)

def test_do_algebra_division_by_zero():
    """Test that division by zero raises the appropriate Python exception."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])
    with pytest.raises(ZeroDivisionError):
        do_algebra(['/'], [10, 0])

def test_do_algebra_mismatched_lengths():
    """Test that mismatched operator and operand lengths raise a ValueError."""
    with pytest.raises(ValueError):
        do_algebra(['+', '-'], [10, 5]) 
    with pytest.raises(ValueError):
        do_algebra(['+'], [10, 5, 2])
    with pytest.raises(ValueError):
        do_algebra([], [])

def test_do_algebra_empty_or_single_inputs():
    """Test edge cases for empty or single-element operand lists."""
    with pytest.raises(ValueError):
        do_algebra([], [10]) 
    with pytest.raises(ValueError):
        do_algebra(['+'], []) 

def test_do_algebra_invalid_operators():
    """Test that unsupported operators raise a ValueError."""
    with pytest.raises(ValueError):
        do_algebra(['%'], [10, 3])
    with pytest.raises(ValueError):
        do_algebra(['abc'], [10, 3])