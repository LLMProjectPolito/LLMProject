import pytest
from your_module import double_the_difference  # Replace your_module

def test_empty_list():
    assert double_the_difference([]) == 0

def test_positive_odd_numbers():
    result = double_the_difference([1, 3, 5])
    expected = 1**2 + 3**2 + 5**2
    assert result == expected

def test_mixed_positive_and_even_numbers():
    """Tests that only odd numbers are squared and summed."""
    result = double_the_difference([1, 2, 3, 4, 5])
    expected = 1**2 + 3**2 + 5**2
    assert result == expected

def test_negative_numbers():
    """Tests that negative odd numbers are squared and summed, and negative even numbers are ignored."""
    result = double_the_difference([-1, -2, -3])
    expected = (-1)**2 + (-3)**2
    assert result == expected

def test_negative_and_positive_numbers():
    """Tests a mix of negative and positive numbers, ensuring only odd numbers are squared."""
    result = double_the_difference([-1, 2, 3, -4, 5])
    expected = (-1)**2 + 3**2 + 5**2
    assert result == expected

def test_zero_in_list():
    result = double_the_difference([0, 1, 2, 3])
    expected = 1**2 + 3**2
    assert result == expected

def test_all_even_numbers():
    """Tests that the function returns 0 when all numbers are even."""
    assert double_the_difference([2, 4, 6]) == 0

def test_all_negative_even_numbers():
    """Tests that the function returns 0 when all numbers are negative and even."""
    assert double_the_difference([-2, -4, -6]) == 0

def test_mixed_negative_even_and_odd_numbers():
    """Tests a mix of negative even and odd numbers."""
    result = double_the_difference([-1, -2, 3, -4, 5])
    expected = (-1)**2 + 3**2 + 5**2
    assert result == expected

def test_single_odd_number():
    result = double_the_difference([7])
    expected = 7**2
    assert result == expected

def test_single_even_number():
    assert double_the_difference([2]) == 0

def test_single_negative_odd_number():
    result = double_the_difference([-1])
    expected = (-1)**2
    assert result == expected

def test_single_negative_even_number():
    assert double_the_difference([-2]) == 0

def test_single_zero():
    assert double_the_difference([0]) == 0

def test_all_zeros():
    """Tests the case where all elements in the list are zero."""
    assert double_the_difference([0, 0, 0]) == 0

def test_floats_in_list():
    with pytest.raises(TypeError):
        double_the_difference([1.5, 2.0, 3.5])

def test_strings_in_list():
    with pytest.raises(TypeError):
        double_the_difference([1, "a", 3])

def test_mixed_types():
    with pytest.raises(TypeError):
        double_the_difference([1, 2.5, "a", 3])

def test_large_numbers():
    result = double_the_difference([1001, 1003])
    expected = 1001**2 + 1003**2
    assert result == expected

def test_edge_case_large_list():
    large_list = list(range(1000))
    expected = sum(x**2 for x in large_list if x % 2 != 0)
    assert double_the_difference(large_list) == expected

def test_very_large_list():
    """Tests with a very large list to check for performance and overflow."""
    large_list = list(range(10000))
    expected = sum(x**2 for x in large_list if x % 2 != 0)
    assert double_the_difference(large_list) == expected

def test_none_in_list():
    with pytest.raises(TypeError):
        double_the_difference([1, None, 3])