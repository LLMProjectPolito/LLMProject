
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
    if len(operand) == 0:
        return None

    if len(operand) == 1:
        return operand[0]

    if len(operator) == 0:
        return None

    if len(operator) == 1:
        return operator[0]

    if len(operator) == 2:
        return operator[0] * operator[1]

    if operator[0] == '+':
        return operand[0] + operand[1]
    elif operator[0] == '-':
        return operand[0] - operand[1]
    elif operator[0] == '*':
        return operand[0] * operand[1]
    elif operator[0] == '/':
        if operand[1] == 0:
            return None
        return operand[0] // operand[1]
    elif operator[0] == '**':
        return operand[0] ** operand[1]
    else:
        return None

def do_algebra_positive(operator, operand):
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
    if len(operand) != 2:
        raise ValueError("Operand must be a list of two integers.")
    
    if operator == ' '+'':
        return operand[0] + operand[1]
    elif operator == '-':
        return operand[0] - operand[1]
    elif operator == '*':
        return operand[0] * operand[1]
    elif operator == '/':
        if operand[1] == 0:
            return None
        return operand[0] // operand[1]
    elif operator == '**':
        return operand[0] ** operand[1]
    else:
        return 0  # Default value for unknown operators


def test_do_algebra_positive():
    assert do_algebra_positive('+', 2) == 2
    assert do_algebra_positive('-', 2) == 2
    assert do_algebra_positive('*', 2) == 4
    assert do_algebra_positive('/', 2) == 1
    assert do_algebra_positive('+', 2, 3) == 9
    assert do_algebra_positive('-', 2, 3) == 3
    assert do_algebra_positive('*', 2, 3) == 6
    assert do_algebra_positive('/', 2, 3) == 1

def test_do_algebra_empty():
    assert do_algebra_positive('', 2) is None
    assert do_algebra_positive('+', 2) is None
    assert do_algebra_positive('-', 2) is None
    assert do_algebra_positive('*', 2) is None
    assert do_algebra_positive('/', 2) is None

def test_do_algebra_positive_example():
    assert do_algebra_positive('+', 2) == 2
    assert do_algebra_positive('-', 2) == 2
    assert do_algebra_positive('*', 2) == 4
    assert do_algebra_positive('/', 2) == 1
    assert do_algebra_positive('+', 2, 3) == 9
    assert do_algebra_positive('-', 2, 3) == 3
    assert do_algebra_positive('*', 2, 3) == 6
    assert do_algebra_positive('/', 2, 3) == 1

def test_do_algebra_negative_example():
    assert do_algebra_positive('-', 2) == -2
    assert do_algebra_positive('*', -2) == -4
    assert do_algebra_positive('/', -2) == 2
    assert do_algebra_positive('+', -2) == -2
    assert do_algebra_positive('-', -2) == -2
    assert do_algebra_positive('-', -2) == 2
    assert do_algebra_positive('*', -2) == -4
    assert do_algebra_positive('/', -2) == 2

def test_do_algebra_zero_division():
    assert do_algebra_positive('+', 0) is None
    assert do_algebra_positive('-', 0) is None
    assert do_algebra_positive('*', 0) is None
    assert do_algebra_positive('/', 0) is None