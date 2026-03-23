import pytest

def test_order_by_points_empty():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([5]) == [5]

def test_order_by_points_basic():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_same_sum():
    assert order_by_points([12, 21, 3, 30]) == [3, 12, 21, 30]
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -10, -11, -2]) == [-1, -2, -10, -11]
    assert order_by_points([-1, -10, -100]) == [-1, -10, -100]

def test_order_by_points_mixed_positive_negative():
    assert order_by_points([1, -1, 10, -10]) == [-1, 1, -10, 10]

def test_order_by_points_large_numbers():
    assert order_by_points([123, 45, 678, 9]) == [9, 45, 123, 678]
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 12345, 6789]

def test_order_by_points_all_same_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_order_by_points_zeroes():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_order_by_points_complex():
    assert order_by_points([23, 1, 4, 12, 5, 6]) == [1, 4, 5, 6, 12, 23]
    assert order_by_points([21, 12, 3, 45, 6]) == [3, 6, 21, 12, 45]
    assert order_by_points([21, 12, 3, 4, 5, 6, 7, 8, 9, 10]) == [3, 21, 12, 4, 5, 6, 7, 8, 9, 10]

def test_order_by_points_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_order_by_points_all_same_digit_sum():
    assert order_by_points([11, 20, 101, 3, 12]) == [3, 11, 20, 12, 101]