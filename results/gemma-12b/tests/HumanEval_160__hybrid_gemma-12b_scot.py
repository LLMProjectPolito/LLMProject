
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

# Basic Operations
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

# Mixed Operators
def test_mixed_operators():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

# Edge Cases
def test_zero_operand_addition():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_zero_operand_multiplication():
    operator = ['*']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 0

def test_large_numbers():
    operator = ['+']
    operand = [1000000, 2000000]
    assert do_algebra(operator, operand) == 3000000

def test_single_operator():
    operator = ['*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 24

# Error Handling
def test_empty_operator_list():
    operator = []
    operand = [2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_operand_list_too_short():
    operator = ['+']
    operand = [2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_mismatched_lengths():
    operator = ['+']
    operand = [2, 3, 4]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_negative_operand():
    operator = ['+']
    operand = [2, -3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_invalid_operator():
    operator = ['&']
    operand = [2, 3]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)