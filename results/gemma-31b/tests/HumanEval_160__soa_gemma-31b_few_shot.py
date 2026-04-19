
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
    (['+'], [1, 2], 3),
    (['-'], [5, 2], 3),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Example from docstring
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    
    # Precedence: Multiplication/Division before Addition/Subtraction
    (['+', '*'], [2, 3, 4], 14),  # 2 + (3 * 4)
    (['-', '*'], [10, 2, 3], 4),   # 10 - (2 * 3)
    (['*', '+'], [2, 3, 4], 10),   # (2 * 3) + 4
    
    # Precedence: Exponentiation before Multiplication/Division
    (['*', '**'], [2, 3, 2], 18),  # 2 * (3 ** 2)
    (['**', '*'], [2, 3, 4], 32),  # (2 ** 3) * 4
    
    # Precedence: Floor division and Exponentiation
    (['//', '**'], [100, 5, 2], 5), # 100 // (5 ** 2) = 100 // 25
    (['**', '//'], [2, 3, 4], 2),   # (2 ** 3) // 4 = 8 // 4
    
    # Complex mixed expressions
    (['+', '*', '//', '**'], [10, 2, 5, 2, 2], 15), # 10 + (2 * 5 // 2**2) = 10 + (10 // 4) = 10 + 2 = 12
    # Wait, let's re-calc: 10 + 2 * 5 // 2**2 
    # 2**2 = 4
    # 2 * 5 = 10
    # 10 // 4 = 2
    # 10 + 2 = 12. Correcting the expected value in the test case below.
    
    # Edge cases: Zeroes
    (['+', '*'], [0, 0, 0], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    (['-'], [0, 10], -10),
    
    # Large numbers
    (['**', '+'], [2, 10, 100], 1124), # 2**10 + 100 = 1024 + 100
])
def test_do_algebra_standard(operators, operands, expected):
    # Note: The complex mixed expression above was corrected to 12 in the logic, 
    # but I will use a simpler one for the actual parametrize list to avoid confusion.
    pass

# Redefining the parametrize list for the actual execution to ensure accuracy
@pytest.mark.parametrize("operators, operands, expected", [
    (['+'], [1, 2], 3),
    (['-'], [5, 2], 3),
    (['*'], [3, 4], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['+', '*'], [2, 3, 4], 14),
    (['-', '*'], [10, 2, 3], 4),
    (['*', '+'], [2, 3, 4], 10),
    (['*', '**'], [2, 3, 2], 18),
    (['**', '*'], [2, 3, 4], 32),
    (['//', '**'], [100, 5, 2], 4), # 100 // 25 = 4
    (['**', '//'], [2, 3, 4], 2),
    (['+', '*', '//', '**'], [10, 2, 5, 2, 2], 12),
    (['+', '*'], [0, 0, 0], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    (['-'], [0, 10], -10),
    (['**', '+'], [2, 10, 100], 1124),
])
def test_do_algebra_execution(operators, operands, expected):
    from solution import do_algebra # Assuming the function is in solution.py or similar
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    from solution import do_algebra
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])