
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

def test_mixed_operations():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_multiple_operands():
    operator = ['+', '*', '//']
    operand = [2, 3, 4, 5, 6]
    assert do_algebra(operator, operand) == 11

def test_zero_operand():
    operator = ['+']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 5

    operator = ['*']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 0

def test_large_numbers():
    operator = ['+']
    operand = [1000000, 2000000]
    assert do_algebra(operator, operand) == 3000000

def test_invalid_operator():
    operator = ['%']
    operand = [2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_incorrect_list_lengths():
    operator = ['+']
    operand = [2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

    operator = ['+', '*']
    operand = [2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_empty_operator_list():
    operator = []
    operand = [2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_single_operand():
    operator = ['+']
    operand = [2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)