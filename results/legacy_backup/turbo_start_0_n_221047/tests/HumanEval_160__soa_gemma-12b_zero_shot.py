import pytest
from your_module import do_algebra  # Replace your_module

def test_do_algebra_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_subtraction():
    operator = ['-']
    operand = [5, 2]
    assert do_algebra(operator, operand) == 3

def test_do_algebra_multiplication():
    operator = ['*']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 6

def test_do_algebra_floor_division():
    operator = ['//']
    operand = [10, 2]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8

def test_do_algebra_complex_expression():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_multiple_operations():
    operator = ['+', '*', '//']
    operand = [2, 3, 4, 2]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_exponentiation_and_multiplication():
    operator = ['*', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 36

def test_do_algebra_large_numbers():
    operator = ['+']
    operand = [1000, 2000]
    assert do_algebra(operator, operand) == 3000

def test_do_algebra_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_negative_result():
    operator = ['-']
    operand = [2, 5]
    assert do_algebra(operator, operand) == -3

def test_do_algebra_multiple_subtractions():
    operator = ['-', '-']
    operand = [10, 3, 2]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_multiple_multiplications():
    operator = ['*', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 24

def test_do_algebra_floor_division_zero_divisor():
    operator = ['//']
    operand = [5, 0]
    with pytest.raises(ZeroDivisionError):
        do_algebra(operator, operand)

def test_do_algebra_exponentiation_zero_base():
    operator = ['**']
    operand = [0, 2]
    assert do_algebra(operator, operand) == 0

def test_do_algebra_exponentiation_negative_exponent():
    operator = ['**']
    operand = [2, -1]
    assert do_algebra(operator, operand) == 0.5

def test_do_algebra_long_expression():
    operator = ['+', '*', '-', '//', '**']
    operand = [1, 2, 3, 4, 5, 2]
    assert do_algebra(operator, operand) == 12