import pytest
import math


# Focus: Operator Precedence
def test_operator_precedence_multiplication_and_addition():
    assert do_algebra(['*', '+'], [2, 3, 4]) == 10

def test_operator_precedence_exponentiation_and_addition():
    assert do_algebra(['**', '+'], [2, 3, 2]) == 11

def test_operator_precedence_multiple_operators():
    assert do_algebra(['+', '*', '-', '//'], [2, 3, 4, 2, 1]) == 8

# Focus: Empty/Invalid Input Lists
def test_algebra_empty_operator():
    with pytest.raises(IndexError):
        do_algebra([], [1, 2])

def test_algebra_empty_operand():
    with pytest.raises(IndexError):
        do_algebra(['+'], [])

def test_algebra_operator_len_mismatch():
    with pytest.raises(IndexError):
        do_algebra(['+'], [1, 2, 3])

# Focus: Large Numbers/Overflow
import pytest

def test_do_algebra_large_numbers():
    operators = ['+', '*', '+']
    operands = [10**9, 10**9, 10**9]
    assert do_algebra(operators, operands) == 3 * 10**9

def test_do_algebra_overflow_exponentiation():
    operators = ['**']
    operands = [2, 32]
    assert do_algebra(operators, operands) == 4294967296

def test_do_algebra_large_numbers_mixed_operations():
    operators = ['+', '*', '-', '//']
    operands = [10**9, 2, 10**9, 2]
    assert do_algebra(operators, operands) == 10**9 + 2 * 10**9 - (10**9 // 2)