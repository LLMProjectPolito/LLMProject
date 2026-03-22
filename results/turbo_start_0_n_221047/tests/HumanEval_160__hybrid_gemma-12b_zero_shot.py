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

def test_do_algebra_long_expression():
    operator = ['+', '*', '-', '//', '**']
    operand = [2, 3, 4, 5, 2, 3]
    assert do_algebra(operator, operand) == 27

def test_do_algebra_zero_operand():
    operator = ['+']
    operand = [0, 5]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_large_numbers():
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

def test_do_algebra_mixed_operations():
    operator = ['*', '+', '//']
    operand = [2, 3, 4, 2]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_negative_result():
    operator = ['-']
    operand = [2, 5]
    assert do_algebra(operator, operand) == -3

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

def test_do_algebra_with_same_operators():
    operator = ['+', '+']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 6

def test_do_algebra_with_same_operands():
    operator = ['*']
    operand = [2, 2]
    assert do_algebra(operator, operand) == 4

def test_do_algebra_exponentiation_and_multiplication():
    operator = ['*', '**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 36

def test_do_algebra_large_numbers_addition():
    operator = ['+']
    operand = [1000, 2000]
    assert do_algebra(operator, operand) == 3000

def test_do_algebra_all_operators():
    operator = ['+', '-', '*', '//', '**']
    operand = [1, 2, 3, 4, 5]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_with_same_numbers():
    operator = ['+']
    operand = [5, 5]
    assert do_algebra(operator, operand) == 10

def test_do_algebra_with_one_operator():
    operator = ['*']
    operand = [1, 1]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_with_zero_and_one():
    operator = ['+']
    operand = [0, 1]
    assert do_algebra(operator, operand) == 1

def test_do_algebra_with_zero_and_zero():
    operator = ['+']
    operand = [0, 0]
    assert do_algebra(operator, operand) == 0