
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """

import pytest

def test_empty_list():
    """Test with an empty list."""
    assert specialFilter([]) == 0

def test_no_special_numbers():
    """Test with a list containing no special numbers."""
    assert specialFilter([2, 4, 6, 8, 10, 12]) == 0

def test_single_special_number():
    """Test with a list containing a single special number."""
    assert specialFilter([15]) == 1

def test_multiple_special_numbers():
    """Test with a list containing multiple special numbers."""
    assert specialFilter([15, 37, 59, 71, 93]) == 5

def test_mixed_numbers():
    """Test with a list containing both special and non-special numbers."""
    assert specialFilter([15, -73, 14, -15]) == 1

def test_more_mixed_numbers():
    """Test with a more complex mix of numbers."""
    assert specialFilter([33, -2, -3, 45, 21, 109]) == 2

def test_negative_numbers():
    """Test with a list of negative numbers."""
    assert specialFilter([-15, -37, -59, -71, -93]) == 0

def test_large_numbers():
    """Test with large numbers."""
    assert specialFilter([111, 333, 555, 777, 999]) == 5

def test_large_numbers_mixed_special():
    """Test with a mix of large numbers, some special and some not."""
    assert specialFilter([111, 222, 333, 444, 555]) == 3

def test_edge_case_11():
    """Test with the edge case 11."""
    assert specialFilter([11]) == 0

def test_edge_case_99():
    """Test with the edge case 99."""
    assert specialFilter([99]) == 1

def test_edge_case_101():
    """Test with the edge case 101."""
    assert specialFilter([101]) == 0

def test_edge_case_1001():
    """Test with the edge case 1001."""
    assert specialFilter([1001]) == 0

def test_zero_as_input():
    """Test with zero as input."""
    assert specialFilter([0]) == 0

def test_special_number_sum_of_digits_multiple_of_3():
    """Test with a number where the sum of digits is a multiple of 3."""
    assert specialFilter([123]) == 1

def test_float_input():
    """Test with float input, expecting a TypeError."""
    with pytest.raises(TypeError):
        specialFilter([15.5])

def test_string_input():
    """Test with string input, expecting a TypeError."""
    with pytest.raises(TypeError):
        specialFilter(["15"])

def test_none_input():
    """Test with None input, expecting a TypeError."""
    with pytest.raises(TypeError):
        specialFilter([None])

def test_bool_input():
    """Test with boolean input, expecting a TypeError."""
    with pytest.raises(TypeError):
        specialFilter([True])

def test_dict_input():
    """Test with dictionary input, expecting a TypeError."""
    with pytest.raises(TypeError):
        specialFilter([{"a": 1}])

def test_empty_string_input():
    """Test with an empty string as input, expecting a TypeError."""
    with pytest.raises(TypeError):
        specialFilter([""])

def test_large_number_boundary():
    """Test with a large number close to the maximum integer size."""
    assert specialFilter([1999999999]) == 1

def test_large_list():
    """Test with a very large list."""
    large_list = [i for i in range(1000)]
    assert specialFilter(large_list) == 50