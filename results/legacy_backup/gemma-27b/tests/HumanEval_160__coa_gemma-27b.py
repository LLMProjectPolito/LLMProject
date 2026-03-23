import pytest
import math


# Focus: Operator Precedence
def test_operator_precedence_multiplication_and_addition():
    assert do_algebra(['*', '+'], [2, 3, 4]) == 10

def test_operator_precedence_exponentiation_and_subtraction():
    assert do_algebra(['**', '-'], [2, 3, 1]) == 7

def test_operator_precedence_floor_division_and_addition():
    assert do_algebra(['//', '+'], [10, 3, 2]) == 5

# Focus: Empty/Invalid Input Lists
def test_empty_operator_list():
    with pytest.raises(ValueError) as excinfo:
        do_algebra([], [1, 2])
    assert "Operator list has at least one operator" in str(excinfo.value)

def test_empty_operand_list():
    with pytest.raises(ValueError) as excinfo:
        do_algebra(['+'], [])
    assert "Operand list has at least two operands" in str(excinfo.value)

def test_operator_len_invalid():
    with pytest.raises(ValueError) as excinfo:
        do_algebra(['+'], [1, 2, 3])
    assert "The length of operator list is equal to the length of operand list minus one" in str(excinfo.value)

# Focus: Large Numbers/Overflow
def test_large_numbers_addition():
    operators = ['+']
    operands = [10**10, 10**10]
    assert do_algebra(operators, operands) == 2 * (10**10)

def test_large_numbers_multiplication():
    operators = ['*']
    operands = [10**5, 10**5]
    assert do_algebra(operators, operands) == 10**10

def test_large_numbers_exponentiation():
    operators = ['**']
    operands = [2, 100]
    assert do_algebra(operators, operands) == 2**100