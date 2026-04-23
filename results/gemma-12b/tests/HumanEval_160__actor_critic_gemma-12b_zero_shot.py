
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
from decimal import Decimal

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

def test_multiplication_exponentiation():
    operator = ['*', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 32

def test_multiple_operators_addition_subtraction():
    operator = ['+', '*', '-', '//']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == -1

def test_floor_division_negative():
    operator = ['//']
    operand = [-10, 3]
    assert do_algebra(operator, operand) == -4

def test_exponentiation_negative_base():
    operator = ['**']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == -8

def test_exponentiation_negative_exponent():
    operator = ['**']
    operand = [2, -2]
    assert do_algebra(operator, operand) == 0.25

def test_addition_float():
    operator = ['+']
    operand = [2.5, 3.5]
    assert do_algebra(operator, operand) == 6.0

def test_subtraction_float():
    operator = ['-']
    operand = [5.5, 2.5]
    assert do_algebra(operator, operand) == 3.0

def test_multiplication_float():
    operator = ['*']
    operand = [2.5, 3.5]
    assert do_algebra(operator, operand) == 8.75

def test_floor_division_float():
    operator = ['//']
    operand = [10.5, 2.5]
    assert do_algebra(operator, operand) == 4

def test_exponentiation_float():
    operator = ['**']
    operand = [2.5, 2.0]
    assert do_algebra(operator, operand) == 6.25

def test_empty_operator_list():
    with pytest.raises(IndexError):
        do_algebra([], [2, 3])

def test_empty_operand_list():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_mismatched_lengths():
    with pytest.raises(IndexError):
        do_algebra(['+', '*'], [2, 3])

def test_invalid_operator():
    with pytest.raises(ValueError):
        do_algebra(['invalid'], [2, 3])

def test_division_by_zero():
    operator = ['//']
    operand = [10, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_large_numbers():
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

def test_exponentiation_zero():
    operator = ['**']
    operand = [2, 0]
    assert do_algebra(operator, operand) == 1

def test_exponentiation_one():
    operator = ['**']
    operand = [5, 1]
    assert do_algebra(operator, operand) == 5

def test_negative_result():
    operator = ['-']
    operand = [2, 5]
    assert do_algebra(operator, operand) == -3

def test_multiple_operators():
    operator = ['+', '-', '*', '//']
    operand = [1, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == -1

def test_long_expression():
    operator = ['+', '*', '-', '//', '**']
    operand = [1, 2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 15

def test_decimal_input():
    operator = ['+']
    operand = [Decimal('2.5'), Decimal('3.5')]
    assert do_algebra(operator, operand) == Decimal('6.0')

def test_type_error():
    operator = ['+']
    operand = ['2', 3]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)

def test_non_integer_result():
    operator = ['/']
    operand = [3, 2]
    assert do_algebra(operator, operand) == 1.5