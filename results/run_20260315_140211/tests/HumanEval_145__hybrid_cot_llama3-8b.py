import pytest
from solution import order_by_points  # assuming the function is in a module named 'solution'

def test_empty_list():
    """Test empty list"""
    assert order_by_points([]) == []

def test_single_element_list():
    """Test single element list"""
    assert order_by_points([1]) == [1]

def test_single_element_list_zero():
    """Test single element list with zero"""
    assert order_by_points([0]) == [0]

def test_duplicate_elements():
    """Test list with duplicate elements"""
    assert order_by_points([1, 11, 1, 11]) == [1, 1, 11, 11]

def test_duplicate_elements_zero():
    """Test list with duplicate elements including zero"""
    assert order_by_points([1, 0, 1, 0]) == [0, 0, 1, 1]

def test_negative_numbers():
    """Test list with negative numbers"""
    assert order_by_points([-1, -11, 1]) == [-1, -11, 1]

def test_negative_numbers_zero():
    """Test list with negative numbers including zero"""
    assert order_by_points([-1, -11, 0, 1]) == [-1, -11, 0, 1]

def test_numbers_with_different_digits():
    """Test list with numbers having different numbers of digits"""
    assert order_by_points([1, 11, 111]) == [1, 11, 111]

def test_numbers_with_same_digit_sum():
    """Test list with numbers having the same digit sum"""
    assert order_by_points([1, 10, 2, 12]) == [1, 2, 10, 12]

def test_numbers_with_same_index():
    """Test list with numbers having the same index in the original list"""
    assert order_by_points([1, 2, 3]) == [1, 2, 3]

def test_numbers_with_same_digit_sum_and_index():
    """Test list with numbers having the same digit sum and index"""
    assert order_by_points([1, 2, 11, 12]) == [1, 2, 11, 12]

def test_large_numbers():
    """Test list with large numbers"""
    assert order_by_points([100, 1000, 10000]) == [100, 1000, 10000]

def test_large_negative_numbers():
    """Test list with large negative numbers"""
    assert order_by_points([-100, -1000, -10000]) == [-100, -1000, -10000]

def test_mixed_numbers():
    """Test list with mixed numbers"""
    assert order_by_points([1, -11, 111, -1]) == [-1, -11, 1, 111]

def test_mixed_numbers_zero():
    """Test list with mixed numbers including zero"""
    assert order_by_points([1, -11, 111, 0, -1]) == [-1, -11, 0, 1, 111]

def test_large_digit_sum():
    """Test list with large digit sum"""
    assert order_by_points([123456, 1234567, 1234]) == [1234, 123456, 1234567]

def test_negative_large_digit_sum():
    """Test list with negative large digit sum"""
    assert order_by_points([-123456, -1234567, -1234]) == [-1234, -123456, -1234567]

def test_order_by_points_empty_list():
    """Test order_by_points with an empty list"""
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    """Test order_by_points with a single element"""
    assert order_by_points([1]) == [1]

def test_order_by_points_duplicate_elements():
    """Test order_by_points with duplicate elements"""
    assert order_by_points([1, 1, 1]) == [1, 1, 1]

def test_order_by_points_negative_numbers():
    """Test order_by_points with negative numbers"""
    assert order_by_points([-1, -11, 1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_zero():
    """Test order_by_points with zero"""
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_order_by_points_large_numbers():
    """Test order_by_points with large numbers"""
    assert order_by_points([100, 1000, 1]) == [1, 100, 1000]

def test_order_by_points_sorted_list():
    """Test order_by_points with a sorted list"""
    assert order_by_points([1, 2, 3]) == [1, 2, 3]

def test_order_by_points_mixed_positive_negative():
    """Test order_by_points with a mixed list of positive and negative numbers"""
    assert order_by_points([1, -1, 11, -11, -12]) == [-1, -11, 1, -12, 11]