import pytest
import math

def test_double_the_difference_with_mixed_types():
    """Test with a list containing mixed types (strings, floats, booleans)"""
    from your_module import double_the_difference  # Replace your_module
    input_list = [1, 2.5, "hello", True, 3, -1, 0]
    expected_result = 1 + 9 + 0
    assert double_the_difference(input_list) == expected_result