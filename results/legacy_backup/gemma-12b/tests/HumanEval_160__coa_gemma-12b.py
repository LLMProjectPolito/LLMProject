import pytest
import math


# Focus: Operator Validation
def test_operator_validation_valid_operators():
    operator = ['+', '*', '//', '**']
    operand = [2, 3, 4, 5]
    assert set(operator) <= {'+', '-', '*', '//', '**'}

def test_operator_validation_invalid_operator():
    operator = ['+', '*', '//', '%']
    operand = [2, 3, 4, 5]
    assert '%' not in operator

def test_operator_validation_empty_operator_list():
    operator = []
    operand = [2, 3]
    assert len(operator) >= 0

# Focus: Operand Value Range
def test_operand_value_range_positive():
    operator = ['+', '*']
    operand = [1, 2, 3]
    assert do_algebra(operator, operand) == 7

def test_operand_value_range_zero():
    operator = ['+']
    operand = [0, 0, 0]
    assert do_algebra(operator, operand) == 0

def test_operand_value_range_large():
    operator = ['*']
    operand = [1000, 1000]
    assert do_algebra(operator, operand) == 1000000

# Focus: Expression Complexity
def test_expression_complexity_simple():
    operator = ['+']
    operand = [1, 2]
    assert do_algebra(operator, operand) == 3

def test_expression_complexity_multiple():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_expression_complexity_exponentiation():
    operator = ['**']
    operand = [2, 3]
    assert do_algebra(operator, operand) == 8