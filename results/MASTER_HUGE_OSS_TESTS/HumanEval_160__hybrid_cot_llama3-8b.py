import pytest
from math import floor

def test_do_algebra_addition():
    array = [2, 3, 4]
    operator = ['+', '*']
    result = do_algebra(operator, array)
    assert result == (2 + 3) * 4

def test_do_algebra_subtraction():
    array = [5, 3, 4]
    operator = ['+', '-']
    result = do_algebra(operator, array)
    assert result == (5 + 3) - 4

def test_do_algebra_multiplication():
    array = [2, 3, 4]
    operator = ['*', '+']
    result = do_algebra(operator, array)
    assert result == 2 * (3 + 4)

def test_do_algebra_floor_division():
    array = [5, 3]
    operator = ['//']
    result = do_algebra(operator, array)
    assert result == floor(5 / 3)

def test_do_algebra_exponentiation():
    array = [2, 3]
    operator = ['**']
    result = do_algebra(operator, array)
    assert result == 2 ** 3

def test_do_algebra_empty_operator():
    array = [2, 3, 4]
    operator = []
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_single_operator():
    array = [2, 3, 4]
    operator = ['+']
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_empty_operand():
    array = []
    operator = ['+', '*']
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_single_operand():
    array = [2]
    operator = ['+', '*']
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_zero_operand():
    array = [0]
    operator = ['+', '*']
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_negative_operand():
    array = [-1]
    operator = ['+', '*']
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_non_integer_operand():
    array = [1.5]
    operator = ['+', '*']
    with pytest.raises(TypeError):
        do_algebra(operator, array)

def test_do_algebra_max_operands():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    operator = ['+', '*', '-', '//', '**']
    result = do_algebra(operator, array)
    assert result == (1 + 2 * 3 - 4 // 5) ** 6 + 7 * 8 - 9

def test_do_algebra_min_operands():
    array = [1, 2]
    operator = ['+', '*']
    result = do_algebra(operator, array)
    assert result == 1 + 2

def test_do_algebra_mismatch_operands():
    array = [1, 2, 3, 4]
    operator = ['+', '*']
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_invalid_operator():
    array = [1, 2]
    operator = ['!=']
    with pytest.raises(ValueError):
        do_algebra(operator, array)

def test_do_algebra_invalid_operand():
    array = [1, 'a']
    operator = ['+', '*']
    with pytest.raises(TypeError):
        do_algebra(operator, array)

def test_do_algebra():
    # Test Case 1: Basic Addition
    assert do_algebra(['+', '*'], [2, 3, 4]) == 14

    # Test Case 2: Basic Subtraction
    assert do_algebra(['-', '*'], [2, 3, 4]) == -10

    # Test Case 3: Basic Multiplication
    assert do_algebra(['*', '-'], [2, 3, 4]) == -10

    # Test Case 4: Basic Floor Division
    assert do_algebra(['//', '-'], [8, 3, 4]) == 0

    # Test Case 5: Basic Exponentiation
    assert do_algebra(['**', '-'], [2, 3, 4]) == -64

    # Test Case 6: Multiple Operators
    assert do_algebra(['+', '-', '*', '//'], [2, 3, 4, 5]) == 9

    # Test Case 7: Invalid Input
    with pytest.raises(ValueError):
        do_algebra(['+', '-', '*'], [2, 3])

    with pytest.raises(ValueError):
        do_algebra(['+', '-', '*'], [2])

    # Test Case 8: Multiple Negatives
    assert do_algebra(['+', '-', '*'], [-2, -3, -4]) == 6