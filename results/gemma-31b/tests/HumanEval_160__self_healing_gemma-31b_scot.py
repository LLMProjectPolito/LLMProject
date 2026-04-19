
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

@pytest.mark.parametrize("operators, operands, expected", [
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['+'], [1, 1], 2),
    (['-'], [10, 5], 5),
    (['*'], [4, 3], 12),
    (['//'], [10, 3], 3),
    (['**'], [2, 3], 8),
    (['+', '*'], [2, 3, 4], 14),
    (['*', '+'], [2, 3, 4], 10),
    (['+', '**'], [2, 3, 2], 11),
    (['**', '+'], [2, 3, 2], 10),
    (['-', '//'], [20, 10, 3], 17),
    (['+', '-', '*'], [1, 2, 3, 4], -9),
    (['*', '//', '**'], [10, 4, 2, 3], 5),
])
def test_do_algebra_standard_cases(operators, operands, expected):
    assert do_algebra(operators, operands) == expected

def test_do_algebra_zero_operands():
    # Testing zeros in operands
    assert do_algebra(['*', '+'], [0, 5, 10]) == 10
    assert do_algebra(['+', '*'], [0, 0, 0]) == 0
    assert do_algebra(['**'], [0, 5]) == 0
    assert do_algebra(['**'], [5, 0]) == 1

def test_do_algebra_large_numbers():
    # Testing larger integers
    assert do_algebra(['+'], [1000000, 2000000]) == 3000000
    assert do_algebra(['**'], [2, 10]) == 1024

def test_do_algebra_minimum_length():
    # Minimum length: 1 operator, 2 operands
    assert do_algebra(['+'], [1, 2]) == 3
    assert do_algebra(['-'], [1, 2]) == -1

def test_do_algebra_floor_division_precision():
    # Ensuring // is used and not /
    assert do_algebra(['//'], [7, 2]) == 3
    assert do_algebra(['//'], [1, 2]) == 0