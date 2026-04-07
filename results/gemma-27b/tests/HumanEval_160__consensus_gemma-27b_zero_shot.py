
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
    result = operand[0]
    for i in range(len(operator)):
        if operator[i] == '+':
            result += operand[i+1]
        elif operator[i] == '-':
            result -= operand[i+1]
        elif operator[i] == '*':
            result *= operand[i+1]
        elif operator[i] == '//':
            result //= operand[i+1]
        elif operator[i] == '**':
            result **= operand[i+1]
    return result

@pytest.mark.parametrize("operator, operand, expected", [
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['+', '-', '*'], [1, 2, 3, 4], 3),
    (['*', '+', '/'], [2, 3, 4, 2], 7.0),
    (['**', '+', '-'], [2, 3, 4, 1], 15),
    (['+', '+', '+'], [1, 2, 3, 4], 10),
    (['-', '-', '-'], [5, 2, 3, 1], 1),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    (['//', '//', '//'], [10, 2, 2, 2], 2),
    (['+', '*'], [1, 2, 3], 7),
    (['-', '/'], [10, 2, 5], 3.0),
    (['**', '+'], [2, 3, 2], 11),
    (['+', '+', '+', '+'], [1, 1, 1, 1, 1], 5),
    (['-', '-', '-', '-'], [5, 1, 1, 1, 1], 1),
    (['*', '*', '*', '*'], [2, 2, 2, 2, 2], 32),
    (['//', '//', '//', '//'], [16, 2, 2, 2, 2], 1),
    (['**', '**', '**'], [2, 2, 2, 2], 65536),
    (['+', '-', '*', '//', '**'], [1, 2, 3, 4, 2], -1),
    (['+', '*', '**'], [2, 3, 2, 2], 20),
    (['-', '/', '+'], [10, 2, 5, 2], 8),
    (['+', '-', '+', '-'], [1, 2, 3, 4, 5], -3),
    (['*', '/', '+', '-'], [2, 4, 2, 1, 1], 2),
    (['**', '+', '-', '*'], [2, 3, 1, 2, 2], 5),
    (['//', '*', '+', '**'], [10, 2, 3, 2, 2], 13),
    (['+', '+'], [1, 2, 3], 6),
    (['-', '-'], [5, 2, 1], 2),
    (['*', '*'], [2, 3, 4], 24),
    (['//', '//'], [10, 2, 2], 2),
    (['**', '**'], [2, 2, 3], 16),
])
def test_do_algebra(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

def test_do_algebra_empty_operator():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2])

def test_do_algebra_empty_operand():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_do_algebra_invalid_operator():
    with pytest.raises(KeyError):
        do_algebra(['%'], [1, 2])

def test_do_algebra_zero_division():
    with pytest.raises(ZeroDivisionError):
        do_algebra(['/'], [1, 0])