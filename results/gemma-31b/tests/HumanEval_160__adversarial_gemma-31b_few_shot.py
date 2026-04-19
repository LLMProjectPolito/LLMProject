
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

def test_do_algebra_basic_operations():
    """ Test basic single-operator expressions to ensure each operator works. """
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-'], [10, 4]) == 6
    assert do_algebra(['*'], [3, 7]) == 21
    assert do_algebra(['//'], [10, 3]) == 3
    assert do_algebra(['**'], [2, 3]) == 8

def test_do_algebra_precedence():
    """ 
    Test mathematical order of operations (PEMDAS).
    The implementation must not simply evaluate left-to-right.
    """
    # Multiplication before Addition: 2 + (3 * 4) - 5 = 9
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    
    # Exponentiation before Multiplication: 2 * (3 ** 2) = 18
    assert do_algebra(['*', '**'], [2, 3, 2]) == 18
    
    # Exponentiation before Subtraction: 10 - (2 ** 3) = 2
    assert do_algebra(['-', '**'], [10, 2, 3]) == 2
    
    # Left-to-right for same precedence: (10 // 2) * 3 = 15
    assert do_algebra(['//', '*'], [10, 2, 3]) == 15

def test_do_algebra_edge_cases():
    """ Test boundary conditions and specific numeric edge cases. """
    # Minimum allowed input size
    assert do_algebra(['+'], [0, 0]) == 0
    
    # Resulting in a negative number (operands are non-negative, but result can be negative)
    assert do_algebra(['-'], [1, 10]) == -9
    
    # Large numbers / Exponentiation
    assert do_algebra(['**', '+'], [2, 10, 5]) == 1029 # (2^10) + 5
    
    # Floor division resulting in 0
    assert do_algebra(['//'], [1, 2]) == 0

def test_do_algebra_division_by_zero():
    """ Ensure the function handles division by zero according to Python standards. """
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])
    
    with pytest.raises(ZeroDivisionError):
        do_algebra(['+', '//'], [5, 10, 0])

@pytest.mark.parametrize("ops, nums, expected", [
    (['+', '+', '+'], [1, 1, 1, 1], 4),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    (['**', '**'], [2, 2, 2], 16), # (2^2)^2 = 16 (Left-associative in Python)
    (['-', '-'], [100, 10, 10], 80),
])
def test_do_algebra_parametrized(ops, nums, expected):
    """ Bulk test for various combinations. """
    assert do_algebra(ops, nums) == expected

def test_do_algebra_invalid_inputs():
    """ 
    Blue Team Security/Robustness check: 
    How does the function handle unexpected input types or operators?
    """
    # Test with an unsupported operator (should ideally raise an error or handle gracefully)
    with pytest.raises((ValueError, SyntaxError, TypeError)):
        do_algebra(['%'], [10, 3])
    
    # Test with non-integer operands (if the function is strictly for ints)
    # This checks if the function crashes or handles type mismatches
    with pytest.raises(TypeError):
        do_algebra(['+'], ["1", 2])