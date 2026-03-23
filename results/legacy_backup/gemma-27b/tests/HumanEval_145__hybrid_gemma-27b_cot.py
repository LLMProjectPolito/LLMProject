import pytest

def test_empty_list():
    assert order_by_points([]) == []

def test_single_element():
    assert order_by_points([5]) == [5]

def test_positive_numbers():
    assert order_by_points([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert order_by_points([1, 11, 2, 22]) == [1, 2, 11, 22]

def test_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]
    assert order_by_points([-1, -11, -2, -22]) == [-1, -2, -11, -22]

def test_mixed_positive_negative():
    assert order_by_points([1, -1, 2, -2, 3, -3]) == [1, -1, 2, -2, 3, -3]
    assert order_by_points([1, -1, 11, -11, -12]) == [-1, 1, -11, 11, -12]

def test_example_case():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_same_digit_sum_different_index():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]
    assert order_by_points([10, 1, 100, 1000]) == [1, 10, 100, 1000]

def test_large_numbers():
    assert order_by_points([1000, 1, 100, 10]) == [1, 10, 100, 1000]
    assert order_by_points([12345, 6789, 10, 1]) == [1, 10, 12345, 6789]

def test_numbers_with_zero():
    assert order_by_points([0, 10, 1, 100]) == [0, 1, 10, 100]

def test_duplicate_numbers():
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]
    assert order_by_points([1, 1, 1, 1]) == [1, 1, 1, 1]

def test_negative_numbers_with_large_digit_sum():
    assert order_by_points([-19, -1, -10]) == [-1, -10, -19]

def test_complex_case():
    assert order_by_points([123, 45, 6, 789, 1, -10, -1]) == [-1, -10, 6, 1, 45, 123, 789]
    assert order_by_points([1, 11, -1, -11, -12, 12, 2, -2]) == [-1, 1, -2, 2, -11, 11, -12, 12]

def test_all_same_digit_sum():
    assert order_by_points([10, 1, 19, 28]) == [1, 10, 19, 28]
    assert order_by_points([1, 10, 100, 1000]) == [1, 10, 100, 1000]

def test_large_negative_numbers():
    assert order_by_points([-1000, -100, -10, -1]) == [-1, -10, -100, -1000]
    assert order_by_points([-12345, -6789, -10, -1]) == [-1, -10, -12345, -6789]

def test_zeroes():
    assert order_by_points([0, 0, 0]) == [0, 0, 0]

def test_negative_zero():
    assert order_by_points([-0, 0]) == [-0, 0]

def test_negative_and_duplicate():
    assert order_by_points([-1, -1, -1, -1]) == [-1, -1, -1, -1]

def test_mixed_duplicates():
    assert order_by_points([1, -1, 1, -1]) == [-1, -1, 1, 1]