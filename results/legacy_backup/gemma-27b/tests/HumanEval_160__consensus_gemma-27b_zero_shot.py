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
    (['**', '-', '+'], [2, 3, 4, 5], 13),
    (['//', '+', '*'], [10, 2, 3, 4], 14),
    (['+'], [1, 2], 3),
    (['-'], [5, 3], 2),
    (['*'], [2, 4], 8),
    (['//'], [10, 5], 2),
    (['**'], [2, 3], 8),
    (['+', '+'], [1, 2, 3], 6),
    (['-', '-'], [5, 2, 1], 2),
    (['*', '*'], [2, 3, 4], 24),
    (['//', '//'], [20, 5, 2], 2),
    (['**', '**'], [2, 2, 2], 16),
    (['+', '*', '-', '//', '**'], [1, 2, 3, 4, 2], -1),
    (['-','*','+'], [10,2,5,3], 13),
    (['+','-','*'], [5,2,3,4], 9),
    (['+', '*', '-'], [2, 3, 4, 5], 9),
    (['+', '-', '*'], [1, 2, 3, 4], 3),
    (['**', '+', '-'], [2, 3, 4, 1], 15),
    (['+', '+', '+'], [1, 2, 3, 4], 10),
    (['-', '-', '-'], [5, 2, 3, 1], 1),
    (['*', '*', '*'], [2, 2, 2, 2], 16),
    (['//', '//', '//'], [16, 2, 2, 2], 1),
    (['+', '*'], [1, 2, 3], 7),
    (['-', '/'], [10, 2, 5], 3.0),
    (['**', '+'], [2, 3, 2], 11),
    (['+', '+', '+', '+'], [1, 1, 1, 1, 1], 5),
    (['-', '-', '-', '-'], [5, 1, 1, 1, 1], 1),
    (['*', '*', '*', '*'], [2, 2, 2, 2, 2], 32),
    (['//', '//', '//', '//'], [16, 2, 2, 2, 2], 1),
    (['**', '**', '**'], [2, 2, 2, 2], 65536),
])
def test_do_algebra(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operand", [
    [1, 2],
    [2, 3, 4],
    [5, 6, 7, 8],
])
def test_operand_length(operand):
    operator = ['+'] * (len(operand) - 1)
    do_algebra(operator, operand)

@pytest.mark.parametrize("operator", [
    ['+'],
    ['-', '*'],
    ['+', '-', '+'],
])
def test_operator_length(operator):
    operand = [1] * (len(operator) + 1)
    do_algebra(operator, operand)

@pytest.mark.parametrize("operand", [
    [0, 1, 2],
    [1, 0, 3],
    [2, 3, 0],
])
def test_zero_operand(operand):
    operator = ['+'] * (len(operand) - 1)
    assert do_algebra(operator, operand) == sum(operand)

@pytest.mark.parametrize("operator, operand", [
    (['//'], [5, 0]),
])
def test_division_by_zero(operator, operand):
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)