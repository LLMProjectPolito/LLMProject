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
    operator = ['+', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_multiple_operations_with_subtraction():
    operator = ['+', '-', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 2 + 3 - 4 * 5

def test_do_algebra_empty_operator_list():
    with pytest.raises(IndexError):
        do_algebra([], [2, 3])

def test_do_algebra_empty_operand_list():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_do_algebra_unequal_length():
    with pytest.raises(IndexError):
        do_algebra(['+', '-'], [2, 3])

def test_do_algebra_invalid_operator():
    with pytest.raises(Exception):
        do_algebra(['%'], [2, 3])

def test_do_algebra_invalid_operand():
    with pytest.raises(Exception):
        do_algebra(['+'], [-2, 3])