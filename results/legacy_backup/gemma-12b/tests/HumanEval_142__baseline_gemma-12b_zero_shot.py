import pytest

def test_empty_list():
    """Test case for an empty list."""
    from your_module import sum_squares  # Replace your_module
    lst = []
    expected = 0
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_one_element():
    """Test case for a list with one element."""
    from your_module import sum_squares  # Replace your_module
    lst = [1]
    expected = 1
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_multiple_elements_no_mod():
    """Test case for a list with multiple elements where no index is a multiple of 3 or 4."""
    from your_module import sum_squares  # Replace your_module
    lst = [1, 2, 3, 4, 5]
    expected = 1 + 2 + 3 + 4 + 5
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_multiple_elements_mod3():
    """Test case for a list with multiple elements where some indices are multiples of 3."""
    from your_module import sum_squares  # Replace your_module
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = 1 + 2 + 9 + 4 + 5 + 36 + 7 + 8 + 81
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_multiple_elements_mod4():
    """Test case for a list with multiple elements where some indices are multiples of 4."""
    from your_module import sum_squares  # Replace your_module
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 1 + 2 + 3 + 64 + 5 + 6 + 7 + 128 + 9 + 10 + 11 + 1728
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_multiple_elements_mod3_and_4():
    """Test case for a list with multiple elements where some indices are multiples of both 3 and 4."""
    from your_module import sum_squares  # Replace your_module
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    expected = 1 + 2 + 9 + 64 + 5 + 6 + 7 + 128 + 9 + 10 + 11 + 1728
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_negative_numbers():
    """Test case for a list with negative numbers."""
    from your_module import sum_squares  # Replace your_module
    lst = [-1, -5, 2, -1, -5]
    expected = -126
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_zeros():
    """Test case for a list with zeros."""
    from your_module import sum_squares  # Replace your_module
    lst = [0, 0, 0, 0, 0]
    expected = 0
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_list_with_mixed_positive_and_negative():
    """Test case with a mix of positive and negative numbers."""
    from your_module import sum_squares  # Replace your_module
    lst = [1, -2, 3, -4, 5]
    expected = 1 + (-2)**2 + 3 + (-4)**3 + 5
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_large_numbers():
    """Test case with large numbers to check for potential overflow issues."""
    from your_module import sum_squares  # Replace your_module
    lst = [1000, 2000, 3000]
    expected = 1000000 + 4000000 + 3000
    actual = sum_squares(lst)
    assert actual == expected, f"Expected {expected}, but got {actual}"