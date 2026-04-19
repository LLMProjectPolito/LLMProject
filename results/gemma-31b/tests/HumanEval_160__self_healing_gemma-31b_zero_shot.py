
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
    expression = str(operand[0])
    for op, val in zip(operator, operand[1:]):
        expression += f" {op} {val}"
    return eval(expression)

import pytest

@pytest.mark.parametrize("operators, operands, expected", [
    # Example from problem description
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    
    # Basic operations (single operator)
    (['+'], [10, 5], 15),
    (['-'], [10, 5], 5),
    (['*'], [10, 5], 50),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    
    # Order of operations (Precedence)
    # 2 + (3 * 4) = 14
    (['+', '*'], [2, 3, 4], 14),
    # (2 * 3) + 4 = 10
    (['*', '+'], [2, 3, 4], 10),
    # 2 + (3 ** 2) = 11
    (['+', '**'], [2, 3, 2], 11),
    # (2 ** 3) + 4 = 12
    (['**', '+'], [2, 3, 4], 12),
    
    # Mixed complex expression
    # 10 + 2 * 3 ** 2 // 4 - 1
    # 10 + 2 * 9 // 4 - 1
    # 10 + 18 // 4 - 1
    # 10 + 4 - 1 = 13
    (['+', '*', '**', '//', '-'], [10, 2, 3, 2, 4, 1], 13),
    
    # Edge cases with zero
    (['*'], [0, 100], 0),
    (['+'], [0, 0], 0),
    (['**'], [0, 5], 0),
    (['**'], [5, 0], 1),
    (['//'], [0, 5], 0),
    
    # Larger numbers
    (['*'], [1000, 1000], 1000000),
    (['**'], [10, 5], 100000),
])
def test_do_algebra(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_division_by_zero():
    """Test that division by zero raises the appropriate error."""
    with pytest.raises(ZeroDivisionError):
        do_algebra(['//'], [10, 0])

def test_do_algebra_large_expression():
    """Test a longer sequence of operations."""
    operators = ['+', '+', '+', '+']
    operands = [1, 1, 1, 1, 1]
    assert do_algebra(operators, operands) == 5