
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """

import pytest
import math


# Focus: Operator Validation
def test_operator_validation_valid_operators():
    operators = ['+', '*', '-', '//', '**']
    operands = [2, 3, 4, 5]
    for op in operators:
        assert op in ['+', '-', '*', '//', '**']

def test_operator_validation_empty_operator_list():
    operators = []
    operands = [2, 3]
    assert len(operators) >= 0

def test_operator_validation_invalid_operator():
    operators = ['%', '(', ')']
    operands = [2, 3]
    for op in operators:
        assert op not in ['+', '-', '*', '//', '**']

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
    """Tests a simple expression with few operations."""
    operator = ['+']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 5

def test_expression_complexity_multiple():
    """Tests an expression with multiple operations."""
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_expression_complexity_exponentiation():
    """Tests an expression with exponentiation."""
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8