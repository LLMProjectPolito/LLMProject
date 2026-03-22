import pytest

def test_order_by_points_empty_list():
    assert order_by_points([]) == []

def test_order_by_points_single_element():
    assert order_by_points([1]) == [1]

def test_order_by_points_already_sorted():
    assert order_by_points([-1, -11, 1, -12, 11]) == [-1, -11, 1, -12, 11]

def test_order_by_points_unsorted():
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]

def test_order_by_points_duplicates():
    assert order_by_points([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

def test_order_by_points_negative_numbers():
    assert order_by_points([-1, -2, -3, -4, -5]) == [-1, -2, -3, -4, -5]

def test_order_by_points_large_numbers():
    assert order_by_points([100, 200, 300, 400, 500]) == [100, 200, 300, 400, 500]

def test_order_by_points_zero():
    assert order_by_points([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_order_by_points_mixed():
    assert order_by_points([1, -1, 0, 10, -10]) == [-1, 0, 1, -10, 10]