
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
from your_module import do_algebra  # Replace your_module

def test_do_algebra_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_do_algebra_multiplication():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_do_algebra_floor_division():
    operator = ['//']
    operand = [10, 2]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_do_algebra_complex_expression():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_multiple_operations():
    operator = ['+', '*', '//']
    operand = [2, 3, 4, 2]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_exponentiation_and_multiplication():
    operator = ['*', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 36

def test_do_algebra_subtraction_and_division():
    operator = ['-', '//']
    operand = [10, 2, 2]
    assert do_algebra(operator, operand) == 4

def test_do_algebra_large_numbers():
    operator = ['+']
    operand = [1000, 2000]
    assert do_algebra(operator, operand) == 3000

def test_do_algebra_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_negative_result():
    operator = ['-']
    operand = [2, 5]
    assert do_algebra(operator, operand) == -3

def test_do_algebra_multiple_operators_and_operands():
    operator = ['+', '*', '-', '//', '**']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 28

def test_do_algebra_all_operators():
    operator = ['+', '-', '*', '//', '**']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 28

def test_do_algebra_long_expression():
    operator = ['+', '*', '-', '//', '**', '+', '*']
    operand = [1, 2, 3, 4, 5, 6, 7]
    assert do_algebra(operator, operand) == 145

def test_do_algebra_with_same_numbers():
    operator = ['+', '+', '+']
    operand = [1, 1, 1]
    assert do_algebra(operator, operand) == 3

def test_do_algebra_with_zero_and_other_numbers():
    operator = ['*']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 0