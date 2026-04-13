
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

# Pytest tests
def test_algebra_basic():
    assert do_algebra(['+', '*', '-'], [2, 3, 4, 5]) == 9

def test_algebra_addition():
    assert do_algebra(['+'], [1, 2]) == 3

def test_algebra_subtraction():
    assert do_algebra(['-'], [5, 2]) == 3

def test_algebra_multiplication():
    assert do_algebra(['*'], [3, 4]) == 12

def test_algebra_floor_division():
    assert do_algebra(['//'], [10, 2]) == 5

def test_algebra_exponentiation():
    assert do_algebra(['**'], [2, 3]) == 8

def test_algebra_complex():
    assert do_algebra(['+', '*', '-', '//', '**'], [1, 2, 3, 4, 5]) == 1 + (2 * 3) - (4 // 5)

def test_algebra_long_chain():
    assert do_algebra(['+', '+', '+', '+'], [1, 2, 3, 4, 5]) == 15

def test_algebra_zero():
    assert do_algebra(['+', '-', '*'], [0, 1, 2, 3]) == -2

def test_algebra_large_numbers():
    assert do_algebra(['*'], [1000, 1000]) == 1000000

def test_algebra_mixed_operators():
    assert do_algebra(['+', '*', '-', '//'], [10, 2, 3, 6]) == 10 + (2 * 3) - (6 // 2)