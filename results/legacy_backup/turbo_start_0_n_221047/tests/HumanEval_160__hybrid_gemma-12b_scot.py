import pytest
from your_module import do_algebra  # Replace your_module

"""
This test suite covers the do_algebra function, testing various arithmetic operations,
edge cases, and error handling scenarios.
"""

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
    operand = [8, 2]
    assert do_algebra(operator, operand) == 4

def test_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_mixed_operations():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_exponentiation_with_multiplication():
    operator = ['*', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 36

def test_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

    operator = ['*']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 0

def test_large_numbers():
    operator = ['+']
    operand = [1000000, 2000000]
    assert do_algebra(operator, operand) == 3000000

    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

def test_single_operator():
    operator = ['+']
    operand = [1, 2]
    assert do_algebra(operator, operand) == 3

def test_invalid_operator():
    operator = ['%']
    operand = [2, 3]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)

    operator = ['&']
    operand = [1, 2]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)

def test_empty_operator_list():
    operator = []
    operand = [2, 3]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)

def test_operand_list_too_short():
    operator = ['+']
    operand = [2]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)

def test_negative_operand():
    operator = ['+']
    operand = [-2, 3]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)