import pytest
import math


# Focus: Operator Validation
def test_operator_validation_valid_operators():
    operators = ['+', '*', '//', '**']
    operands = [2, 3, 4, 5]
    assert all(op in ['+', '-', '*', '//', '**'] for op in operators)

def test_operator_validation_invalid_operator():
    operators = ['+', '*', '%', '**']
    operands = [2, 3, 4, 5]
    assert '%' not in operators

def test_operator_validation_empty_operator_list():
    operators = []
    operands = [2, 3]
    assert len(operators) == 0

# Focus: Operand Value Range
def test_operand_value_range_positive():
    """Test with positive operand values within a reasonable range."""
    operator = ['+', '*', '-']
    operand = [1, 2, 3, 4]
    assert do_algebra(operator, operand) == 1 + 2 * 3 - 4
    assert do_algebra(operator, operand) == -1

def test_operand_value_range_zero():
    """Test with operand values including zero."""
    operator = ['+', '*', '//']
    operand = [0, 5, 2]
    assert do_algebra(operator, operand) == 0 + 5 * 2
    assert do_algebra(operator, operand) == 10

def test_operand_value_range_large():
    """Test with larger operand values to check for potential overflow issues."""
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000 * 1000
    assert do_algebra(operator, operand) == 1000000

# Focus: Expression Complexity
def test_expression_complexity_simple():
    """Tests a simple expression with minimal complexity."""
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_expression_complexity_multiple_operations():
    """Tests an expression with multiple operations."""
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_expression_complexity_exponentiation():
    """Tests an expression with exponentiation."""
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8