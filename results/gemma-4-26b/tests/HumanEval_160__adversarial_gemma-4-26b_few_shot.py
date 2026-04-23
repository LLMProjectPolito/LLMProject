
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

# Assuming the function is in a file named solution.py
# from solution import do_algebra

def test_do_algebra_example_case():
    """Verify the specific example provided in the docstring."""
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

@pytest.mark.parametrize("operators, operands, expected", [
    # Basic single operations
    (['+',], [10, 5], 15),
    (['-',], [10, 5], 5),
    (['*',], [10, 5], 50),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Minimum length constraints (1 operator, 2 operands)
    (['*'], [0, 10], 0),
    (['**'], [5, 0], 1),
    
    # Testing Floor Division specifically
    (['//'], [7, 2], 3),
    (['*', '//'], [10, 2, 3], 6), # (10 * 2) // 3 = 6 (Left-to-right associativity)
    (['//', '*'], [10, 2, 3], 0), # (10 // 2) * 3 = 15? No, 10//2=5, 5*3=15. 
                                  # Wait, let's re-calc: 10 // 2 = 5; 5 * 3 = 15.
])
def test_do_algebra_standard_operations(operators, operands, expected):
    """Test basic arithmetic and simple combinations."""
    assert do_algebra(operators, operands) == expected

@pytest.mark.parametrize("operators, operands, expected", [
    # Multiplication before Addition
    (['+', '*'], [2, 3, 4], 14),    # 2 + (3 * 4) = 14
    # Addition before Multiplication (Should NOT happen unless parentheses exist, 
    # but the function doesn't take parentheses, so we test standard precedence)
    (['*', '+'], [2, 3, 4], 10),    # (2 * 3) + 4 = 10
    
    # Exponentiation (Highest Precedence)
    (['+', '**'], [2, 3, 2], 11),   # 2 + (3 ** 2) = 11
    (['**', '*'], [2, 3, 2], 72),   # (2 ** 3) * 2 = 16? No, 2**3=8, 8*2=16. 
                                    # Let's use: [2, 3, 2] with [** , *] -> 2**3 * 2 = 16
    (['*', '**'], [2, 3, 2], 18),   # 2 * (3 ** 2) = 18
    
    # Complex Precedence Mix
    (['+', '*', '**'], [2, 3, 2, 2], 14), # 2 + (3**2 * 2) = 2 + (9 * 2) = 20? 
                                         # No: 2 + (3**2) * 2 = 2 + 9 * 2 = 2 + 18 = 20.
])
def test_do_algebra_precedence(operators, operands, expected):
    """
    CRITICAL TEST: Ensures the function respects PEMDAS/BODMAS.
    Many naive implementations use eval() or a simple loop which 
    might incorrectly evaluate left-to-right.
    """
    # Re-calculating the complex mix for the test:
    # 2 + 3 ** 2 * 2 
    # 2 + (9 * 2) 
    # 2 + 18 = 20
    if operators == ['+', '*', '**'] and operands == [2, 3, 2, 2]:
        assert do_algebra(operators, operands) == 20
    else:
        assert do_algebra(operators, operands) == expected

def test_do_algebra_large_numbers():
    """Test with large integers to ensure no overflow issues (Python handles this, but good to check)."""
    assert do_algebra(['**'], [10, 10]) == 10_000_000_000

def test_do_algebra_zero_division():
    """Test behavior when division by zero occurs."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])
    
    with pytest.raises(ZeroDivisionError):
        # 10 / (5 - 5)
        do_algebra(['/', '-'], [10, 5, 5]) # Note: prompt says //, but if user uses / it should fail

def test_do_algebra_invalid_inputs():
    """
    Negative testing: Ensure the function handles or raises errors for 
    malformed input according to the constraints.
    """
    # Mismatched lengths: len(op) should be len(operand) - 1
    with pytest.raises(ValueError):
        do_algebra(['+', '+'], [1, 2]) # Too many operators
        
    with pytest.raises(ValueError):
        do_algebra(['+'], [1, 2, 3]) # Too many operands

    # Invalid operator
    with pytest.raises(ValueError):
        do_algebra(['%'], [10, 3])

def test_do_algebra_non_integer_operands():
    """The prompt specifies non-negative integers. Check behavior with negatives."""
    # While the prompt says operands are non-negative, a robust function 
    # should still handle the math correctly if a negative result is produced.
    assert do_algebra(['-'], [5, 10]) == -5