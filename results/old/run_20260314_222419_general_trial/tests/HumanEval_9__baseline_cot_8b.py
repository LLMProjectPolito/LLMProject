import pytest

def test_rolling_max_empty_list():
    assert rolling_max([]) == []

def test_rolling_max_single_element():
    assert rolling_max([1]) == [1]

def test_rolling_max_increasing_sequence():
    assert rolling_max([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_rolling_max_decreasing_sequence():
    assert rolling_max([5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

def test_rolling_max_mixed_sequence():
    assert rolling_max([1, 2, 3, 2, 3, 4, 2]) == [1, 2, 3, 3, 3, 4, 4]

def test_rolling_max_negative_numbers():
    assert rolling_max([-1, -2, -3, -2, -3, -4, -2]) == [-1, -1, -1, -1, -1, -1, -1]

def test_rolling_max_zero():
    assert rolling_max([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]

def test_rolling_max_large_numbers():
    assert rolling_max([1000, 2000, 3000, 2000, 3000, 4000, 2000]) == [1000, 2000, 3000, 3000, 3000, 4000, 4000]

def test_rolling_max_duplicate_max():
    assert rolling_max([1, 2, 2, 3, 3, 3, 2]) == [1, 2, 2, 3, 3, 3, 3]