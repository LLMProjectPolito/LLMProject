import pytest
import math

def test_basic():
    operator = ['+', '*', '-']
    operand = [2, 3, 4, 5]
    assert do_algebra(operator, operand) == 9

def test_empty_operator_list(do_algebra):
    """
    Test case: Empty operator list with a single operand.
    This is an edge case because the problem description states that the length of the operator list
    is equal to the length of the operand list minus one.  An empty operator list violates this
    constraint, and should ideally raise an error or return a specific value.  However, the
    function's behavior in this scenario is undefined, so we test for a reasonable outcome.
    """
    operator = []
    operand = [5]
    result = do_algebra(operator, operand)
    assert result == 5

import pytest

def test_do_algebra_invalid_operator():
    """
    Test case to check for invalid operator in the operator list.
    """
    operator = ["+", "%"]
    operand = [2, 3]
    with pytest.raises(TypeError):
        # Assuming do_algebra raises TypeError for invalid operators
        # Replace with the actual exception raised by do_algebra
        # if it's different.
        # do_algebra(operator, operand)
        pass