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
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 36

def test_division_by_zero():
    operator = ['//']
    operand = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_large_numbers():
    operator = ['*']
    operand = [1000000, 1000000]
    assert do_algebra(operator, operand) == 1000000000000

def test_zero_operands():
    operator = ['+']
    operand = [0, 0]
    assert do_algebra(operator, operand) == 0

    operator = ['-']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 5

def test_invalid_operator():
    operator = ['&']
    operand = [2, 3]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_empty_lists():
    operator = []
    operand = [2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)

def test_single_operand():
    operator = ['+']
    operand = [2]
    with pytest.raises(ValueError):
        do_algebra(operator, operand)