import pytest
import math

def test_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_edge_empty_operator(do_algebra):
    """
    Test case: Empty operator list with a single operand.
    This is an edge case because the problem description states that the length of the operator list
    is equal to the length of the operand list minus one.  An empty operator list violates this.
    We expect a TypeError because we can't evaluate an expression with no operators.
    """
    try:
        result = do_algebra([], [5])
        assert False, "Expected TypeError was not raised"
    except TypeError:
        pass
    except Exception as e:
        assert False, f"Unexpected exception: {e}"

import pytest

def test_do_algebra_empty_operator():
    """Test with an empty operator list."""
    operator = []
    operand = [5]
    with pytest.raises(ZeroDivisionError):
        from main import do_algebra
        do_algebra(operator, operand)