
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

# Parameterized test for basic arithmetic operations
@pytest.mark.parametrize(
    "operator, operand, expected",
    [
        ("+", [2, 3], 5),
        ("-", [5, 2], 3),
        ("*", [2, 3], 6),
        ("//", [10, 2], 5),
        ("**", [2, 3], 8),
        ("%", [10, 3], 1),  # Added modulus operator
    ],
)
def test_basic_operations(operator, operand, expected):
    assert do_algebra(operator, operand) == expected

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
    assert do_algebra(operator, operand) == 5

def test_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_large_numbers():
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

def test_multiple_operators():
    operator = ['+', '+', '+']
    operand = [1, 2, 3, 4]
    assert do_algebra(operator, operand) == 10

def test_exponentiation_with_zero():
    operator = ['**']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 1

def test_floor_division_with_zero():
    operator = ['//']
    operand = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_negative_result():
    operator = ['-']
    operand = [2, 5]
    assert do_algebra(operator, operand) == -3

def test_mixed_operators():
    operator = ['*', '+', '//']
    operand = [2, 3, 4, 2]
    assert do_algebra(operator, operand) == 10

def test_long_expression():
    operator = ['+', '*', '-', '//', '**']
    operand = [1, 2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 15

# Error Handling Tests
def test_invalid_operator_type():
    operator = [1]
    operand = [2, 3]
    with pytest.raises(TypeError):  # Or ValueError, depending on implementation
        do_algebra(operator, operand)

def test_invalid_operator_symbol():
    operator = ['@']
    operand = [2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_empty_operator_list():
    operator = []
    operand = [2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_empty_operand_list():
    operator = ['+']
    operand = []
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_single_operand():
    operator = ['+']
    operand = [5]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_operator_length_mismatch():
    operator = ['+', '*']
    operand = [2, 3, 4]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

# Floating-Point Tests
def test_floating_point_addition():
    operator = ['+']
    operand = [2.5, 3.5]
    assert do_algebra(operator, operand) == 6.0

def test_floating_point_multiplication():
    operator = ['*']
    operand = [2.5, 3.5]
    assert do_algebra(operator, operand) == 8.75

def test_floating_point_division():
    operator = ['//']
    operand = [7.5, 2.5]
    assert do_algebra(operator, operand) == 3

def test_floating_point_exponentiation():
    operator = ['**']
    operand = [2.0, 3.0]
    assert do_algebra(operator, operand) == 8.0

# Negative Operand Tests
def test_negative_operand_addition():
    operator = ['+']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == 1

def test_negative_operand_multiplication():
    operator = ['*']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == -6

def test_negative_operand_division():
    operator = ['//']
    operand = [-7, 2]
    assert do_algebra(operator, operand) == -4

def test_negative_operand_exponentiation():
    operator = ['**']
    operand = [-2, 3]
    assert do_algebra(operator, operand) == -8

def test_negative_exponent():
    operator = ['**']
    operand = [2, -3]
    assert do_algebra(operator, operand) == 0.125

def test_zero_base_negative_exponent():
    operator = ['**']
    operand = [0, -1]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_single_operator():
    operator = ['+']
    operand = [5, 5]
    assert do_algebra(operator, operand) == 10

def test_string_operator():
    operator = ['+']
    operand = [5, 5]
    assert do_algebra(operator, operand) == 10