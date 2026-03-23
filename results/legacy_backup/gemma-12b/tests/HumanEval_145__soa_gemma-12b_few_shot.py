import pytest

def sum_digits(n):
    s = 0
    for digit in str(abs(n)):
        s += int(digit)
    return s

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_same_digit_sum():
    assert order_by_points([1, 10, 100]) == [1, 10, 100]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 10, -10]) == [1, -1, 10, -10]

def test_order_by_points_complex_example():
    assert order_by_points([23, 1, 5, 12, 3]) == [1, 3, 5, 12, 23]

def test_order_by_points_with_zeros():
    assert order_by_points([0, 10, 2, 1]) == [0, 1, 2, 10]

def test_order_by_points_large_numbers():
    assert order_by_points([12345, 6789, 10]) == [10, 12345, 6789]

def test_order_by_points_duplicate_sums():
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]