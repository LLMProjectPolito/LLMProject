
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
    (['-', '+', '*'], [10, 5, 2, 3], 11),
    (['*'], [2, 3], 6),
    (['+'], [5, 10], 15),
    (['-'], [10, 5], 5),
    (['//'], [10, 2], 5),
    (['**'], [2, 3], 8),
    (['+', '+'], [1, 2, 3], 6),
    (['-', '-'], [10, 2, 3], 5),
    (['*', '*'], [2, 3, 4], 24),
    (['//', '//'], [20, 2, 5], 2),
    (['**', '**'], [2, 2, 2], 16),
    (['+', '*', '-', '//'], [1, 2, 3, 4, 2], 3),
    (['**', '+', '*'], [2, 3, 4, 5], 89),
    (['+', '-', '*', '//', '**'], [1, 2, 3, 4, 5, 2], -1),
])
def test_do_algebra(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operand", [
    [0, 1, 2],
    [10, 20, 30, 40],
    [1, 1, 1, 1, 1]
])
def test_do_algebra_non_negative_operands(operand):
    assert all(x >= 0 for x in operand)

@pytest.mark.parametrize("operator, operand", [
    (['+'], [1]),
    (['*'], [1, 0]),
    (['//'], [10, 0])
])
def test_do_algebra_zero_division(operator, operand):
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

@pytest.mark.parametrize("operator, operand", [
    (['+'], [1, 2, 3]),
    (['*'], [1, 2, 3])
])
def test_do_algebra_invalid_length(operator, operand):
    with pytest.raises(IndexError):
        do_algebra(operator, operand)