import pytest
import math

def test_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert 9 == do_algebra(operator, operand)

def test_edge_empty_operator():
    """Test with an empty operator list and two operands."""
    from your_module import do_algebra  # Replace your_module
    operator = []
    operand = [5, 5]
    result = do_algebra(operator, operand)
    assert result == 10

def test_do_algebra_invalid_operator():
    """Test with an invalid operator in the operator list."""
    operator = ["%", 1, "+"]
    operand = [2, 3, 4]
    try:
        from main import do_algebra
        do_algebra(operator, operand)
        assert False, "Should have raised a TypeError"
    except TypeError:
        assert True