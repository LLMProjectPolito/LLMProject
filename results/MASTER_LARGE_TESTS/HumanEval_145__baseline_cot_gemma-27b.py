import pytest

def test_basic_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_empty_list():
    assert order_by_points([]) == []

def test_list_with_zeros():
    assert order_by_points([0, 10, 0, -10]) == [0, 0, -10, 10]

def test_identical_digit_sums():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_large_numbers():
    assert order_by_points([12345, 6789, 100000, 54321]) == [100000, 12345, 54321, 6789]

def test_negative_numbers():
    assert order_by_points([-1, -11, -111, -1111]) == [-1, -11, -111, -1111]

def test_mixed_positive_and_negative_identical_sums():
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_edge_cases_leading_zeros():
    assert order_by_points([10, 100, 1]) == [1, 10, 100]

def test_boundary_cases():
    assert order_by_points([2147483647, -2147483648, 1]) == [-2147483648, 1, 2147483647]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 11, 11]) == [1, 1, 11, 11]

def test_single_element_list():
    assert order_by_points([5]) == [5]

def test_negative_and_positive_with_same_digit_sum():
    assert order_by_points([-5, 5, 14, -14]) == [-5, 5, -14, 14]