import pytest
import math


# Focus: Operator Precedence
import pytest

def test_operator_precedence_multiplication_and_addition():
    operators = ['+', '*']
    operands = [2, 3, 4]
    expected = 2 + 3 * 4
    assert do_algebra(operators, operands) == expected

def test_operator_precedence_exponentiation_and_addition():
    operators = ['+', '**']
    operands = [2, 3, 2]
    expected = 2 + 3 ** 2
    assert do_algebra(operators, operands) == expected

def test_operator_precedence_subtraction_and_multiplication():
    operators = ['-', '*']
    operands = [5, 2, 3]
    expected = 5 - 2 * 3
    assert do_algebra(operators, operands) == expected

# Focus: Empty/Invalid Input Lists
import pytest

def test_empty_operator_list():
    """Test case for an empty operator list."""
    operator = []
    operand = [2, 3]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_empty_operand_list():
    """Test case for an empty operand list."""
    operator = ['+']
    operand = []
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

def test_operator_length_invalid():
    """Test case where operator list length is not operand length - 1."""
    operator = ['+', '*']
    operand = [2, 3]
    with pytest.raises(IndexError):
        do_algebra(operator, operand)

# Focus: Large Numbers/Overflow
import pytest

def test_large_numbers_addition() -> None:
    operators = ['+']
    operands = [10**18, 10**18]
    expected = 2 * (10**18)
    assert do_algebra(operators, operands) == expected

def test_large_numbers_multiplication() -> None:
    operators = ['*']
    operands = [10**9, 10**9]
    expected = 10**18
    assert do_algebra(operators, operands) == expected

def test_large_numbers_mixed_operations() -> None:
    operators = ['+', '*', '-', '//']
    operands = [10**9, 2, 10**9, 2]
    expected = (10**9 + 2 * 10**9) - (10**9 // 2)
    assert do_algebra(operators, operands) == expected