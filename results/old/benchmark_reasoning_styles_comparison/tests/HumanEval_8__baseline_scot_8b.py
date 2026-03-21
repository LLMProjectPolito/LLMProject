import pytest
from your_module import sum_product  # replace 'your_module' with the actual module name

def test_empty_list():
    """Test sum_product with an empty list."""
    assert sum_product([]) == (0, 1)

def test_single_element_list():
    """Test sum_product with a list containing a single element."""
    assert sum_product([5]) == (5, 5)

def test_multiple_elements_list():
    """Test sum_product with a list containing multiple elements."""
    assert sum_product([1, 2, 3, 4]) == (10, 24)

def test_negative_numbers_list():
    """Test sum_product with a list containing negative numbers."""
    assert sum_product([-1, -2, -3, -4]) == (-10, 24)

def test_mixed_numbers_list():
    """Test sum_product with a list containing mixed numbers."""
    assert sum_product([-1, 2, -3, 4]) == (2, -24)

def test_zero_list():
    """Test sum_product with a list containing zeros."""
    assert sum_product([0, 0, 0]) == (0, 0)

def test_large_numbers_list():
    """Test sum_product with a list containing large numbers."""
    assert sum_product([1000, 2000, 3000]) == (6000, 6000000000)

def test_invalid_input():
    """Test sum_product with invalid input."""
    with pytest.raises(TypeError):
        sum_product("123")

def test_non_integer_input():
    """Test sum_product with non-integer input."""
    with pytest.raises(TypeError):
        sum_product([1.5, 2.5, 3.5])