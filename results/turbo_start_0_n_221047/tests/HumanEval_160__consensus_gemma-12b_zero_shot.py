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

def test_multiplication_exponentiation():
    operator = ['*', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 32

def test_complex_expression():
    operator = ['+', '*', '-', '//']
    operand = [2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 7

def test_large_numbers():
    operator = ['*']
    operand = [1000, 2000]
    assert do_algebra(operator, operand) == 2000000

def test_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_multiple_operators():
    operator = ['+', '-', '*', '//']
    operand = [1, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == -1

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
    operand = [1, 2]
    assert do_algebra(operator, operand) == -1