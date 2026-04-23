
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
    expression = ""
    for i, op in enumerate(operator):
        expression += str(operand[i])
        if op == '+':
            expression += '+'
        elif op == '-':
            expression += '-'
        elif op == '*':
            expression += '*'
        elif op == '//':
            expression += '//'
        elif op == '**':
            expression += '**'
    return eval(expression)


@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, 3], 5),
    (["+", 2, 3, 4], 9),
    (["-", 2, 3], -1),
    (["*", 2, 3], 6),
    (["//", 2, 3], 0),
    (["**", 2, 3], 8),
    (["+", 2, 3, 4, 5], 14),
    (["-", 2, 3, 4, 5], -2),
    (["*", 2, 3, 4, 5], 60),
    (["//", 2, 3, 4, 5], 0),
    (["**", 2, 3, 4, 5], 16),
    (["+", 1, 2, 3], 6),
    (["-", 1, 2, 3], -4),
    (["*", 1, 2, 3], 6),
    (["//", 1, 2, 3], 0),
    (["**", 1, 2, 3], 9),
    ([], [1, 2, 3], 0),  # Empty operator list
    (["+", 1, 2], 3),  # Basic case
    (["*", 1, 2, 3], 6), #Multiplication
    (["//", 1, 2, 3], 0), #Floor division
    (["**", 1, 2, 3], 9) #Exponentiation
])
def test_do_algebra(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 0, 0], 0),
    (["-", 0, 0], 0),
    (["*", 0, 0], 0),
    (["//", 0, 0], 0),
    (["**", 0, 0], 0),
    (["+", 1, 0], 1),
    (["-", 1, 0], -1),
    (["*", 1, 0], 0),
    (["//", 1, 0], 0),
    (["**", 1, 0], 1)
])
def test_do_algebra_zero(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", -1, 1], 0),
    (["-", -1, 1], -2),
    (["*", -1, 1], -1),
    (["//", -1, 1], 0),
    (["**", -1, 1], 1)
])
def test_do_algebra_negative(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 1, 2, 3], 6),
    (["-", 1, 2, 3], -4),
    (["*", 1, 2, 3], 6),
    (["//", 1, 2, 3], 0),
    (["**", 1, 2, 3], 9),
])
def test_do_algebra_longer_expression(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

@pytest.mark.parametrize("operator, operand, expected", [
    (["+", 2, 3, 4, 5], 21),
    (["-", 2, 3, 4, 5], -14),
    (["*", 2, 3, 4, 5], 120),
    (["//", 2, 3, 4, 5], 0),
    (["**", 2, 3, 4, 5], 24)
])
def test_do_algebra_longer_expression_3(operator, operand, expected):
    assert do_algebra(operator, operand) == expected