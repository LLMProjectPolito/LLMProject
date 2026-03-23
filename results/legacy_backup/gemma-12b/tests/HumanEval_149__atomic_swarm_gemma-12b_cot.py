import pytest
import math

def test_sorted_list_sum():
    from solution import sorted_list_sum
    input_list = ["aa", "a", "aaa"]
    expected_output = ["aa"]
    assert sorted_list_sum(input_list) == expected_output

def test_empty_list():
    """Test with an empty list as input."""
    from solution import sorted_list_sum
    assert sorted_list_sum([]) == []

def test_sorted_list_sum_invalid_input_type():
    """Test with a list containing non-string elements."""
    import pytest
    with pytest.raises(TypeError):
        sorted_list_sum([1, "a", 2])