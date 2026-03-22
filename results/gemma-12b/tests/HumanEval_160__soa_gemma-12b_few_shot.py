import pytest

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
    operand = [8, 2]
    assert do_algebra(operator, operand) == 4

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

def test_do_algebra_zero_values():
    operator = ['+', '*']
    operand = [0, 0, 5]
    assert do_algebra(operator, operand) == 0

def test_do_algebra_negative_result():
    operator = ['-']
    operand = [1, 2]
    assert do_algebra(operator, operand) == -1