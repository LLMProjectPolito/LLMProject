import pytest

def test_do_algebra_empty_operator_list():
    """
    Test case for an empty operator list with two operands.
    This is an edge case because the problem statement specifies that the operator list has at least one operator.
    However, it's important to test how the function handles this invalid input.
    """
    with pytest.raises(TypeError):
        do_algebra([], [2, 3])

def test_do_algebra_empty_operator_list_single_operand():
    """
    Test case for an empty operator list with a single operand.
    This is an edge case because the problem statement specifies that the operator list has at least one operator.
    However, it's important to test how the function handles this invalid input.
    """
    with pytest.raises(TypeError):
        do_algebra([], [5])

def test_do_algebra_empty_operator_list_alternative():
    """Test case for an empty operator list with two operands."""
    operator = []
    operand = [5, 2]
    with pytest.raises(TypeError):
        do_algebra(operator, operand)