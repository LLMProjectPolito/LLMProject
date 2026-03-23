import pytest
import math


# Focus: Operator Validation
def test_operator_validation_valid_operators():
    """Test that only valid operators are present."""
    valid_operators = ['+', '-', '*', '//', '**']
    invalid_operators = ['%', '/', '>', '<']
    
    for op in invalid_operators:
        try:
            do_algebra([op], [1, 2])
            assert False, f"Invalid operator '{op}' should have raised an error."
        except Exception as e:
            pass  # Expected error

def test_operator_validation_mixed_operators():
    """Test that a mix of valid operators works correctly."""
    operators = ['+', '*', '//', '-']
    operands = [2, 3, 4, 5]
    result = do_algebra(operators, operands)
    assert result == 2 + 3 * 4 - 5
    assert result == 9

def test_operator_validation_empty_operator_list():
    """Test that an empty operator list raises an error."""
    try:
        do_algebra([], [1, 2])
        assert False, "Empty operator list should have raised an error."
    except Exception as e:
        pass  # Expected error

# Focus: Operand Value Range
import pytest

def test_operand_value_range_positive():
    """Test with positive operand values within a reasonable range."""
    operator = ['+', '*', '-']
    operand = [1, 2, 3, 4]
    assert do_algebra(operator, operand) == 9

def test_operand_value_range_zero():
    """Test with operand values including zero."""
    operator = ['+', '*', '//']
    operand = [0, 5, 2]
    assert do_algebra(operator, operand) == 10

def test_operand_value_range_large():
    """Test with larger operand values to check for potential overflow issues."""
    operator = ['+', '*']
    operand = [1000, 2000]
    assert do_algebra(operator, operand) == 3000

# Focus: Expression Complexity
import pytest
from your_module import do_algebra  # Replace your_module

def test_do_algebra_simple_addition():
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_do_algebra_multiplication_and_addition():
    operator = ['*', '+']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_do_algebra_exponentiation_and_subtraction():
    operator = ['**', '-']
    operand = [2, 3, 1]
    assert do_algebra(operator, operand) == 7