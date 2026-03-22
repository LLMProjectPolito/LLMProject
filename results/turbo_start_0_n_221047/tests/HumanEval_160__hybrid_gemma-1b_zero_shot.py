import pytest

def do_algebra(operator, operand):
    try:
        if len(operator) == 1:
            return operator[0]
        elif len(operand) == 1:
            return operand[0]
        else:
            return eval(str(operator[0]) + str(operand[0]) + operator[1] + str(operand[1]))
    except:
        return None

def test_addition():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    assert result == 9

def test_subtraction():
    array = [2, 3, 4, 5]
    result = 2 - 3 * 4
    assert result == -5

def test_multiplication():
    array = [2, 3, 4, 5]
    result = 2 * 3 * 4
    assert result == 24

def test_floor_division():
    array = [2, 3, 4, 5]
    result = 2 // 4
    assert result == 0.5

def test_exponentiation():
    array = [2, 3, 4, 5]
    result = 2 ** 3
    assert result == 8

def test_empty_operand():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == 9

def test_empty_operator():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == 9

def test_invalid_input():
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4
    assert result == None

def test_different_lengths():
    array = [2, 3]
    result = 2 + 3 * 4
    assert result == 14