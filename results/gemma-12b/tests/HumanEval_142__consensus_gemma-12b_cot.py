


def sum_squares(lst):
    """"
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """

import pytest

def test_empty_list():
    """Test case for an empty list."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([]) == 0

def test_basic_list():
    """Test case for a basic list with some multiples of 3 and 4."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([1, 2, 3]) == 14

def test_list_with_negative_numbers():
    """Test case for a list containing negative numbers."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_list_with_mixed_numbers():
    """Test case for a list with a mix of positive and negative numbers."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([1, -2, 3, -4, 5, -6]) == -12

def test_list_with_only_multiples_of_3():
    """Test case for a list where all elements are at multiples of 3."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([3, 6, 9, 12]) == 234

def test_list_with_only_multiples_of_4():
    """Test case for a list where all elements are at multiples of 4."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([4, 8, 12, 16]) == 424

def test_list_with_multiples_of_both_3_and_4():
    """Test case for a list with elements at multiples of both 3 and 4."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]) == 426

def test_list_with_zero():
    """Test case for a list containing zero."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([0, 1, 2, 3, 4]) == 30

def test_large_list():
    """Test case for a larger list to check performance and correctness."""
    from your_module import sum_squares  # Replace your_module
    large_list = list(range(1, 21))
    expected_sum = 0
    for i, num in enumerate(large_list):
        if i % 3 == 0:
            expected_sum += num**2
        elif i % 4 == 0:
            expected_sum += num**3
        else:
            expected_sum += num
    assert sum_squares(large_list) == expected_sum

def test_list_with_floats():
    """Test case to ensure the function handles floats correctly (should still work as ints)."""
    from your_module import sum_squares  # Replace your_module
    assert sum_squares([1.0, 2.0, 3.0]) == 14.0