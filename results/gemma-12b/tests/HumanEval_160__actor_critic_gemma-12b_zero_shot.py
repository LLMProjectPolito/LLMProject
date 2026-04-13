
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

def test_addition_before_multiplication():
    operator = ['+', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_subtraction_before_division():
    operator = ['-', '//']
    operand = [10, 2, 3]
    assert do_algebra(operator, operand) == 2

def test_complex_expression_precedence():
    operator = ['+', '*', '-', '//']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 5

def test_multiple_additions():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

def test_multiple_subtractions():
    operator = ['-', '-']
    operand = [10, 2, 4]
    assert do_algebra(operator, operand) == 4

def test_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_zero_operator():
    operator = ['*']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 0

def test_large_numbers():
    operator = ['+']
    operand = [1000000, 2000000]
    assert do_algebra(operator, operand) == 3000000

def test_division_by_one():
    operator = ['//']
    operand = [10, 1]
    assert do_algebra(operator, operand) == 10

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

def test_negative_operand_addition():
    operator = ['+']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == 1

def test_negative_operand_subtraction():
    operator = ['-']
    operand = [5, -2]
    assert do_algebra(operator, operand) == 7

def test_negative_operand_multiplication():
    operator = ['*']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == -6

def test_negative_operand_division():
    operator = ['//']
    operand = [-10, 2]
    assert do_algebra(operator, operand) == -5

def test_mixed_integer_float_addition():
    operator = ['+']
    operand = [2, 3.5]
    assert do_algebra(operator, operand) == 5.5

def test_mixed_integer_float_multiplication():
    operator = ['*']
    operand = [2.5, 3]
    assert do_algebra(operator, operand) == 7.5

def test_operator_length_greater_than_operand_length_minus_one():
    operator = ['+', '*', '/']
    operand = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_repeated_unsupported_operators():
    operator = ['^', '^']
    operand = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_operator_at_beginning():
    operator = ['*', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 5

def test_operator_at_end():
    operator = ['+', '*']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 7

def test_exponentiation_negative_base():
    operator = ['**']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == -8

def test_exponentiation_multiple_operators():
    operator = ['+', '*', '**']
    operand = [1, 2, 3, 4]
    assert do_algebra(operator, operand) == 11

def test_operators_of_same_precedence():
    operator = ['*', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 24

def test_single_operand_error_message():
    operator = []
    operand = [5]
    with pytest.raises(ValueError) as excinfo:
        do_algebra(operator, operand)
    assert "Operator list cannot be empty" in str(excinfo.value)

def test_empty_operator_list_error_message():
    operator = []
    operand = [1, 2]
    with pytest.raises(ValueError) as excinfo:
        do_algebra(operator, operand)
    assert "Operator list cannot be empty" in str(excinfo.value)

def test_empty_operand_list_error_message():
    operator = ['+']
    operand = []
    with pytest.raises(ValueError) as excinfo:
        do_algebra(operator, operand)
    assert "Operand list must contain at least two operands" in str(excinfo.value)