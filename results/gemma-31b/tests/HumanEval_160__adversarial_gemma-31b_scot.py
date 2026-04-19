
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

# The function do_algebra is already defined in the environment.
# We are writing the test suite to detect bugs in its implementation.

@pytest.mark.parametrize("operators, operands, expected", [
    # Provided example: 2 + 3 * 4 - 5 = 2 + 12 - 5 = 9
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    
    # Basic operations
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Operator Precedence: Multiplication before Addition
    (['+', '*'], [2, 3, 4], 14), # 2 + (3 * 4)
    (['*', '+'], [2, 3, 4], 10), # (2 * 3) + 4
    
    # Operator Precedence: Exponentiation before Multiplication
    (['*', '**'], [2, 3, 2], 18), # 2 * (3 ** 2) = 2 * 9
    (['**', '*'], [2, 3, 2], 16), # (2 ** 3) * 2 = 8 * 2
    
    # Operator Precedence: Exponentiation before Floor Division
    (['//', '**'], [100, 2, 5], 4), # 100 // (2 ** 5) = 100 // 32 = 3
    
    # Negative results
    (['-'], [5, 10], -5),
    (['-', '+'], [5, 10, 2], -3), # 5 - 10 + 2 = -3
    
    # Zero handling
    (['*'], [10, 0], 0),
    (['+'], [0, 0], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1), # Any number to power 0 is 1
    
    # Minimal input
    (['+'], [1, 1], 2),
])
def test_do_algebra_success(operators, operands, expected):
    """Test various valid algebraic combinations and precedence."""
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    """Test that floor division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_complex_precedence():
    """
    Test a complex expression to ensure Python's evaluation order is followed.
    Expression: 2 ** 3 + 10 // 3 * 2 - 1
    Evaluation: 
    1. 2 ** 3 = 8
    2. 10 // 3 = 3
    3. 3 * 2 = 6
    4. 8 + 6 - 1 = 13
    """
    operators = ['**', '+', '//', '*', '-']
    operands = [2, 3, 10, 3, 2, 1]
    assert do_algebra(operators, operands) == 13

def test_do_algebra_large_numbers():
    """Test exponentiation with larger results."""
    # 2 ** 10 = 1024
    assert do_algebra(['**'], [2, 10]) == 1024

def test_do_algebra_floor_division_precision():
    """Ensure floor division does not return a float."""
    result = do_algebra(['//'], [7, 2])
    assert result == 3
    assert isinstance(result, int)