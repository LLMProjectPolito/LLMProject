import pytest
from your_module import do_algebra  # Replace your_module

def test_addition():
    operators = ['+']
    operands = [1, 2]
    assert do_algebra(operators, operands) == 3

def test_subtraction():
    operators = ['-']
    operands = [5, 3]
    assert do_algebra(operators, operands) == 2

def test_multiplication():
    operators = ['*']
    operands = [2, 4]
    assert do_algebra(operators, operands) == 8

def test_floor_division():
    operators = ['//']
    operands = [12, 3]
    assert do_algebra(operators, operands) == 4

def test_exponentiation():
    operators = ['**']
    operands = [2, 3]
    assert do_algebra(operators, operands) == 8

def test_exponentiation_chained():
    operators = ['**', '**']
    operands = [2, 3, 4]
    assert do_algebra(operators, operands) == 256

def test_mixed_operators():
    operators = ['+', '*', '-']
    operands = [2, 3, 4, 5]
    assert do_algebra(operators, operands) == 15

def test_exponentiation_mixed():
    operators = ['+', '**']
    operands = [2, 3, 2]
    assert do_algebra(operators, operands) == 10

def test_zero_operand():
    operators = ['*']
    operands = [5, 0]
    assert do_algebra(operators, operands) == 0

def test_single_operand():
    operators = []
    operands = [7]
    assert do_algebra(operators, operands) == 7

def test_single_operand_no_operators():
    operators = []
    operands = []
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_large_numbers():
    operators = ['+']
    operands = [10**10, 10**10]
    assert do_algebra(operators, operands) == 2 * 10**10

def test_empty_operator_list():
    operators = []
    operands = [1, 2, 3]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_invalid_operator():
    operators = ['&']
    operands = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_division_by_zero():
    operators = ['/']
    operands = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operators, operands)

def test_negative_numbers():
    operators = ['+', '-', '*', '//', '**']
    operands = [-2, 3, -4, 2, -1]
    assert do_algebra(operators, operands) == 6

def test_floating_point_numbers():
    operators = ['+', '-', '*', '//', '**']
    operands = [1.5, 2.5, 3.5, 4.5]
    assert do_algebra(operators, operands) == 7.5

def test_operator_length_mismatch_more_operators():
    operators = ['+', '*', '//']
    operands = [1, 2]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)

def test_operator_length_mismatch_more_operands():
    operators = ['+']
    operands = [1, 2, 3, 4]
    with pytest.raises(ValueError):
        do_algebra(operators, operands)