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

def test_do_algebra_large_numbers():
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

def test_do_algebra_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_negative_result():
    operator = ['-']
    operand = [2, 5]
    assert do_algebra(operator, operand) == -3

def test_do_algebra_long_expression():
    operator = ['+', '*', '-', '//', '**']
    operand = [1, 2, 3, 4, 5, 6]
    assert do_algebra(operator, operand) == 17

def test_do_algebra_all_positive():
    operator = ['+', '*', '//', '**']
    operand = [1, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == 31

def test_do_algebra_division_by_one():
    operator = ['//']
    operand = [5, 1]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_exponentiation_zero():
    operator = ['**']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_exponentiation_one():
    operator = ['**']
    operand = [5, 1]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_mixed_operations():
    operator = ['+', '-', '*', '//', '**']
    operand = [10, 5, 2, 1, 3]
    assert do_algebra(operator, operand) == 17