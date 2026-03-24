
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

def test_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_multiplication():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_floor_division():
    operator = ['//']
    operand = [10, 2]
    assert do_algebra(operator, operand) == 5

def test_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_addition_multiplication():
    operator = ['+', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_subtraction_division():
    operator = ['-', '//']
    operand = [10, 2, 3]
    assert do_algebra(operator, operand) == 2

def test_complex_expression():
    operator = ['+', '*', '-', '//']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 7

def test_multiple_additions():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

def test_multiple_subtractions():
    operator = ['-', '-']
    operand = [10, 2, 4]
    assert do_algebra(operator, operand) == 4

def test_exponentiation_multiplication():
    operator = ['**', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 72

def test_large_numbers():
    operator = ['*']
    operand = [1000, 2000]
    assert do_algebra(operator, operand) == 2000000

def test_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_zero_operator():
    operator = ['*']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 0

def test_negative_result():
    operator = ['-']
    operand = [2, 5]
    assert do_algebra(operator, operand) == -3

def test_floor_division_zero_divisor():
    operator = ['//']
    operand = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)