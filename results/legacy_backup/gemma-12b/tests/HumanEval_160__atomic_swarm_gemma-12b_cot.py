import pytest
import math

def test_do_algebra_positive():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_empty_operator_list():
    """Test with an empty operator list and two operands."""
    try:
        from main import do_algebra
        operator = []
        operand = [5, 5]
        result = do_algebra(operator, operand)
        assert result == 10
    except Exception as e:
        assert False, f"Test failed with exception: {e}"

import pytest

def test_do_algebra_empty_operator():
    with pytest.raises(ZeroDivisionError):
        do_algebra([], [5])