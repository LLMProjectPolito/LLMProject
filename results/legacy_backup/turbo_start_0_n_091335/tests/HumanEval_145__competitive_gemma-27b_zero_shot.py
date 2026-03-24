import pytest

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_numbers():
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [1, -1, 2, -2, 3, -3]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_same_digit_sum_different_index():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]

def test_large_numbers():
    assert order_by_points([1000, 10, 1, 100]) == [1, 10, 100, 1000]

def test_negative_large_numbers():
    assert order_by_points([-1000, -10, -1, -100]) == [-1, -10, -100, -1000]

def test_zeroes():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_mixed_with_zeroes():
    assert order_by_points([0, 1, -1, 0, 2]) == [-1, 0, 0, 1, 2]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_duplicate_numbers_with_different_sums():
    assert order_by_points([11, 1, 11, 1]) == [1, 1, 11, 11]

def test_complex_case():
    assert order_by_points([23, 12, 5, 1, 34, -1, -23]) == [-1, 1, 5, 12, 23, -23, 34]