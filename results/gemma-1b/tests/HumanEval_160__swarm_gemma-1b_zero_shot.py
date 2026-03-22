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
        if len(operand) == 1:
            return operand[0]
        elif len(operator) == 1:
            return operator[0]
        else:
            return operator[0] * operand[1]
    except:
        return None

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
        if len(operand) == 1:
            return operand[0]
        elif len(operator) == 1:
            return operator[0]
        else:
            return eval(str(operand[0]) + str(operator[0]))
    except (TypeError, ValueError, IndexError):
        return None

def test_do_algebra():
    assert do_algebra('+', [1, 2, 3]) == 9
    assert do_algebra('-', [1, 2, 3]) == 6
    assert do_algebra('*', [1, 2, 3]) == 6
    assert do_algebra('/', [1, 2, 3]) == 1
    assert do_algebra('/', [1, 2, 3]) == 1
    assert do_algebra('+', [1, 2, 3]) == 6
    assert do_algebra('-', [1, 2, 3]) == 6
    assert do_algebra('*', [1, 2, 3]) == 6
    assert do_algebra('/', [1, 2, 3]) == 1
    assert do_algebra('/', [1, 2, 3]) == 1
    assert do_algebra('+', [1, 2]) == 3
    assert do_algebra('-', [1, 2]) == 2
    assert do_algebra('*', [1, 2]) == 2
    assert do_algebra('/', [1, 2]) == 1
    assert do_algebra('+', [1]) == 1
    assert do_algebra('-', [1]) == 1
    assert do_algebra('*', []) == 0
    assert do_algebra('/', []) == 0
    assert do_algebra('+', []) == None
    assert do_algebra('-', []) == None
    print("All tests passed!")

test_do_algebra()