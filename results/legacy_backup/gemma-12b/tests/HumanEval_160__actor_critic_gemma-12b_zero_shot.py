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

def test_exponentiation_addition():
    operator = ['**', '+']
    operand = [2, 3, 1]
    assert do_algebra(operator, operand) == 9

def test_modulo():
    operator = ['%']
    operand = [10, 3]
    assert do_algebra(operator, operand) == 1

def test_floating_point_division():
    operator = ['/']
    operand = [10.0, 2.0]
    assert do_algebra(operator, operand) == 5.0

def test_floating_point_exponentiation():
    operator = ['**']
    operand = [2.0, 3.0]
    assert do_algebra(operator, operand) == 8.0

def test_negative_numbers_in_complex_expression():
    operator = ['+', '*', '-']
    operand = [-2, 3, 4]
    assert do_algebra(operator, operand) == 5

def test_modulo_negative_numbers():
    operator = ['%']
    operand = [-10, 3]
    assert do_algebra(operator, operand) == -1

def test_modulo_floating_point():
    operator = ['%']
    operand = [10.5, 3.2]
    assert do_algebra(operator, operand) == 1.7

def test_mixed_integer_float_operands():
    operator = ['+']
    operand = [2, 3.5]
    assert do_algebra(operator, operand) == 5.5

def test_large_numbers():
    operator = ['*']
    operand = [1000000, 2]
    assert do_algebra(operator, operand) == 2000000

def test_repeated_operators():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

def test_invalid_operator_character():
    invalid_operators = ['a', '$', '#', '%', '&', '^', '(', ')', '[', ']', '{', '}', ';', ':', '<', '>', '?']
    for op in invalid_operators:
        operator = [op]
        operand = [1, 2]
        with pytest.raises(ValueError):
            do_algebra(operator, operand)

def test_empty_operator_list():
    operator = []
    operand = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_empty_operand_list():
    operator = ['+']
    operand = []
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_mismatched_operator_operand_lengths():
    operator = ['+']
    operand = [1, 2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

    operator = ['+', '+']
    operand = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_division_by_zero():
    operator = ['/']
    operand = [1, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

    operator = ['//']
    operand = [1, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_complex_expression_nested():
    operator = ['+', '*', '//', '**']
    operand = [2, 3, 4, 2, 3]
    assert do_algebra(operator, operand) == 17

def test_operator_precedence_multiplication_division():
    operator = ['*', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_operator_precedence_exponentiation():
    operator = ['**', '+']
    operand = [2, 3, 1]
    assert do_algebra(operator, operand) == 9

def test_complex_expression_long():
    operator = ['+', '*', '-', '//', '**', '%']
    operand = [2, 3, 4, 5, 2, 3]
    assert do_algebra(operator, operand) == 13