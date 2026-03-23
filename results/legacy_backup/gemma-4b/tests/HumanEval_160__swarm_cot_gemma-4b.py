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
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 9

def test_subtraction():
    operator = ['-', '-', '-']
    operand = [10, 5, 2, 1]
    assert do_algebra(operator, operand) == 4

def test_multiplication():
    operator = ['*', '*', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 120

def test_floor_division():
    operator = ['//', '//', '//']
    operand = [10, 5, 2, 1]
    assert do_algebra(operator, operand) == 2

def test_exponentiation():
    operator = ['**', '**', '**']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 16

def test_mixed_operations():
    operator = ['+', '*', '-', '**', '//']
    operand = [2, 3, 4, 5, 6, 7]
    assert do_algebra(operator, operand) == 10