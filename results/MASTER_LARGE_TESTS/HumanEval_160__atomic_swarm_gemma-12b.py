import pytest
import math

def test_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_edge_empty_operator():
    """Test with an empty operator list and two operands."""
    operator = []
    operand = [5, 5]
    try:
        from do_algebra import do_algebra
        do_algebra(operator, operand)
    except ZeroDivisionError:
        assert True
    except Exception as e:
        assert False

def test_do_algebra_empty_operator():
    """Test with an empty operator list."""
    try:
        from main import do_algebra
        operator = []
        operand = [5]
        do_algebra(operator, operand)
        assert False, "Expected ValueError not raised"
    except ValueError as e:
        assert str(e) == "Operator list cannot be empty."