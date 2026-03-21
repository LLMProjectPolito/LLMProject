import pytest

def test_do_algebra_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_subtraction():
    operator = ['-']
    operand = [5, 3]
    assert do_algebra(operator, operand) == 2

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

def test_do_algebra_multiple_operations():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_do_algebra_invalid_operator():
    operator = ['^']
    operand = [2, 3]
    with pytest.raises(Exception):
        do_algebra(operator, operand)

def test_do_algebra_invalid_operand():
    operator = ['+']
    operand = [2, 'a']
    with pytest.raises(Exception):
        do_algebra(operator, operand)

def test_do_algebra_empty_operator():
    operator = []
    operand = [2, 3]
    with pytest.raises(Exception):
        do_algebra(operator, operand)

def test_do_algebra_empty_operand():
    operator = ['+']
    operand = []
    with pytest.raises(Exception):
        do_algebra(operator, operand)

def test_do_algebra_unequal_length():
    operator = ['+', '*']
    operand = [2, 3]
    with pytest.raises(Exception):
        do_algebra(operator, operand)