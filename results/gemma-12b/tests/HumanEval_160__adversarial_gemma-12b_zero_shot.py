
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

def test_valid_expression():
    operators = ['+', '*', '-']
    operands = [2, 3, 4, 5]
    assert do_algebra(operators, operands) == 9

def test_addition_only():
    operators = ['+']
    operands = [1, 2, 3]
    assert do_algebra(operators, operands) == 6

def test_subtraction_only():
    operators = ['-']
    operands = [5, 4, 3]
    assert do_algebra(operators, operands) == -2

def test_multiplication_only():
    operators = ['*']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 24

def test_floor_division_only():
    operators = ['//']
    operands = [10, 2, 1]
    assert do_algebra(operators, operands) == 5

def test_exponentiation_only():
    operators = ['**']
    operands = [2, 3, 2]
    assert do_algebra(operators, operands) == 9

def test_mixed_operators():
    operators = ['+', '-', '*', '//', '**']
    operands = [2, 3, 4, 5, 6]
    assert do_algebra(operators, operands) == 2 + 3 - 4 * 5 // 6 ** 2

def test_single_operand_list():
    operators = ['+']
    operands = [5, 5]
    assert do_algebra(operators, operands) == 10

def test_zero_values():
    operators = ['+']
    operands = [0, 0, 0]
    assert do_algebra(operators, operands) == 0

def test_large_numbers():
    operators = ['*']
    operands = [1000, 1000]
    assert do_algebra(operators, operands) == 1000000

def test_negative_result():
    operators = ['-']
    operands = [1, 2]
    assert do_algebra(operators, operands) == -1

def test_floor_division_zero():
    operators = ['//']
    operands = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operators, operands)

def test_exponentiation_negative_base():
    operators = ['**']
    operands = [-2, 3]
    assert do_algebra(operators, operands) == -8

def test_exponentiation_zero_exponent():
    operators = ['**']
    operands = [2, 0]
    assert do_algebra(operators, operands) == 1

def test_exponentiation_negative_exponent():
    operators = ['**']
    operands = [2, -2]
    assert do_algebra(operators, operands) == 0.25

def test_empty_operator_list():
    operators = []
    operands = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_operator_list_longer_than_operand_list():
    operators = ['+', '*']
    operands = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)