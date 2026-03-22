import pytest
import math


# Focus: Operator Validation
def test_operator_validation_valid_operators():
    """
    Test that the function handles valid operators correctly.
    """
    operator = ['+', '*', '//', '**']
    operand = [2, 3, 4, 5]
    assert all(op in ['+', '-', '*', '//', '**'] for op in operator)

def test_operator_validation_invalid_operator():
    """
    Test that the function raises an error when an invalid operator is present.
    """
    operator = ['+', '*', '%', '**']
    operand = [2, 3, 4, 5]
    try:
        all(op in ['+', '-', '*', '//', '**'] for op in operator)
        assert False, "Should have raised an error"
    except ValueError:
        pass
    except Exception as e:
        assert False, f"Unexpected exception: {e}"

def test_operator_validation_empty_operator_list():
    """
    Test that the function handles an empty operator list correctly.
    """
    operator = []
    operand = [2, 3]
    try:
        all(op in ['+', '-', '*', '//', '**'] for op in operator)
        assert False, "Should have raised an error"
    except ValueError:
        pass
    except Exception as e:
        assert False, f"Unexpected exception: {e}"

# Focus: Operand Value Range
import pytest

def test_operand_value_range_positive():
    """Test with positive operand values within a reasonable range."""
    operator = ['+', '*']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 7

def test_operand_value_range_large():
    """Test with larger positive operand values to check for overflow or unexpected behavior."""
    operator = ['+']
    operand = [1000000, 2000000]
    assert do_algebra(operator, operand) == 3000000

def test_operand_value_range_zero():
    """Test with zero as an operand to ensure correct handling."""
    operator = ['*']
    operand = [5, 0]
    assert do_algebra(operator, operand) == 0

# Focus: Expression Complexity
import pytest

def test_expression_complexity_simple():
    """
    Tests a simple expression with a few operators and operands.
    Focuses on ensuring basic arithmetic operations are handled correctly.
    """
    operator = ['+', '*']
    operand = [2, 3, 4]
    assert do_algebra(operator, operand) == 14

def test_expression_complexity_mixed_operations():
    """
    Tests an expression with a mix of different operators.
    Checks for correct order of operations and handling of various arithmetic operations.
    """
    operator = ['+', '-', '*']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_expression_complexity_exponentiation():
    """
    Tests an expression involving exponentiation.
    Verifies that exponentiation is handled correctly within the expression.
    """
    operator = ['*','**']
    operand = [2, 3, 2]
    assert do_algebra(operator, operand) == 12