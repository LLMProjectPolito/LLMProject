
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

def test_addition():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

def test_subtraction():
    operator = ['-', '-', '+']
    operand = [5, 2, 1, 3]
    assert do_algebra(operator, operand) == 3

def test_multiplication():
    operator = ['*', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 60

def test_floor_division():
    operator = ['//', '//']
    operand = [10, 2, 5, 3]
    assert do_algebra(operator, operand) == 2

def test_exponentiation():
    operator = ['**', '**']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 16

def test_mixed_operations():
    operator = ['+', '*', '-', '**']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 26

def test_complex_expression():
    operator = ['+', '*', '//', '-']
    operand = [10, 2, 5, 3, 1, 2]
    assert do_algebra(operator, operand) == 13

def test_single_operand():
    operator = ['+']
    operand = [5]
    assert do_algebra(operator, operand) == 5

def test_empty_operator():
    operator = []
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 1

def test_empty_operand():
    operator = ['+']
    operand = []
    assert do_algebra(operator, operand) == 0

def test_large_numbers():
    operator = ['*', '**']
    operand = [2, 3, 10]
    assert do_algebra(operator, operand) == 240

def test_zero_operand():
    operator = ['+', '*']
    operand = [5, 0, 2]
    assert do_algebra(operator, operand) == 10

def test_floor_division_zero():
    operator = ['//']
    operand = [10, 0, 2]
    assert do_algebra(operator, operand) == 0

def test_exponentiation_zero():
    operator = ['**']
    operand = [2, 0, 3]
    assert do_algebra(operator, operand) == 1