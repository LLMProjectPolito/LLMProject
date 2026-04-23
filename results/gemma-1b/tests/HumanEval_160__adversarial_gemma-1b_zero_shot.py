
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
    try:
        if len(operator) == 1:
            return operator[0]
        elif len(operand) == 1:
            return operand[0]
        else:
            return eval(str(operator[0]) + str(operand[0]) + operator[1] + str(operand[1]))
    except (TypeError, ValueError, IndexError):
        return None

import sys
def test_basic_operations():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert do_algebra(['+', '-', '*'], [1, 2, 3]) == 9
    assert do_algebra(['+', '-', '*'], [1, 2]) == 3
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4]) == 21
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5]) == 15
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6]) == 30
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7]) == 35
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8]) == 42
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9]) == 45
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 48
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == 51
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 54
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]) == 57
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) == 60
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]) == 63
    assert do_algebra(['+', '-', '*'], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 66
    print("All tests passed!")

def test_empty_operand():
    assert do_algebra(['+', '*', '-'], []) is None

def test_empty_operator():
    assert do_algebra([], ['+', '*', '-']) is None