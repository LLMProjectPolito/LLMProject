
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
import math

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
    try:
        if len(operand) == 1 and len(operator) == 1:
            return operator[0] * operand[0]
        elif len(operand) == 1:
            return operand[0]
        elif len(operator) == 1:
            return operator[0]
        elif len(operand) == 2:
            return operand[0] * operator[1]
        elif len(operand) == 2:
            return operand[0] * operator[1]
        elif len(operator) == 3:
            return operator[0] * operand[1] * operand[2]
        elif len(operand) == 3:
            return operand[0] * operator[1] * operator[2]
        else:
            return 0
    except:
        return 0

def do_algebra(operator, operand):
    try:
        if len(operand) == 1:
            return operand[0]
        elif len(operator) == 1:
            return operator[0]
        else:
            return eval(str(operand[0]) + str(operator[0]))
    except (TypeError, ValueError, IndexError):
        return None

def test_do_algebra():
    assert do_algebra('+', [2, 3, 4, 5]) == 14
    assert do_algebra('-', [2, 3, 4, 5]) == -1
    assert do_algebra('*', [2, 3, 4, 5]) == 12
    assert do_algebra('/', [2, 3, 4, 5]) == 2
    assert do_algebra('/', [2, 3, 4, 5]) == 1
    assert do_algebra('-', [2, 3, 4, 5]) == 0
    assert do_algebra('+', [2, 3, 4, 5]) == 2
    assert do_algebra('-', [2, 3, 4, 5]) == 0
    assert do_algebra('+', [2, 3, 4, 5]) == 6
    assert do_algebra('+', [2, 3, 4]) == 24
    assert do_algebra('+', [2, 3, 4, 5]) == 30
    assert do_algebra('+', [2, 3, 4, 5, 6]) == 60
    assert do_algebra('+', [2, 3, 4, 5, 6]) == 120
    assert do_algebra('+', [2, 3, 4]) == 24
    assert do_algebra('+', [2, 3]) == 6
    assert do_algebra('+', [2]) == 2
    assert do_algebra('+', [2, 3, 4]) == 24
    assert do_algebra('+', [2, 3, 4, 5]) == 40
    assert do_algebra('+', [2, 3, 4, 5, 6]) == 60
    assert do_algebra('+', [2, 3, 4, 5, 6]) == 120
    print("All tests passed!")