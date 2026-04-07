
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

def test_addition_only():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_subtraction_only():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_multiplication_only():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_floor_division_only():
    operator = ['//']
    operand = [8, 2]
    assert do_algebra(operator, operand) == 4

def test_exponentiation_only():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_mixed_operators():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_exponentiation_with_multiplication():
    operator = ['*', '**']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 72

def test_zero_operand():
    operator = ['/']
    operand = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_large_numbers():
    operator = ['*']
    operand = [1000000, 1000000]
    assert do_algebra(operator, operand) == 1000000000000

def test_negative_numbers():
    operator = ['-']
    operand = [5, -2]
    assert do_algebra(operator, operand) == 7

def test_empty_lists():
    operator = []
    operand = [2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_invalid_operator():
    operator = ['@']
    operand = [2, 3]
    with pytest.raises(SyntaxError):
        do_algebra(operator, operand)

def test_single_operand():
    operator = ['+']
    operand = [2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_different_data_types():
    operator = ['+']
    operand = [2, 'a']
    with pytest.raises(TypeError):
        do_algebra(operator, operand)