import pytest

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [1, -1, 2, -2, 3, -3]

def test_same_digit_sum_different_index():
    assert order_by_points([11, 2, 1, 20]) == [1, 2, 11, 20]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_larger_numbers():
    assert order_by_points([123, 45, 6, 789, 10]) == [6, 10, 45, 123, 789]

def test_negative_larger_numbers():
    assert order_by_points([-123, -45, -6, -789, -10]) == [-6, -10, -45, -123, -789]

def test_mixed_larger_numbers():
    assert order_by_points([123, -45, 6, -789, 10]) == [6, 10, -45, 123, -789]

def test_zero():
    assert order_by_points([0, 1, 10]) == [0, 1, 10]

def test_multiple_zeros():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_negative_zero():
    assert order_by_points([-0, 1, 10]) == [-0, 1, 10]

def test_large_negative_and_positive():
    assert order_by_points([1000, -1000, 1, -1]) == [1, -1, -1000, 1000]