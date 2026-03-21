import pytest

def test_empty_list():
    assert intersperse([], 4) == []

def test_single_element_list():
    assert intersperse([1], 4) == [1]

def test_multiple_element_list():
    assert intersperse([1, 2, 3], 4) == [1, 4, 2, 4, 3]

def test_large_list():
    numbers = list(range(10))
    expected = [0, 4, 1, 4, 2, 4, 3, 4, 4, 4, 5, 4, 6, 4, 7, 4, 8, 4, 9]
    assert intersperse(numbers, 4) == expected

def test_negative_numbers():
    assert intersperse([-1, -2, -3], 4) == [-1, 4, -2, 4, -3]

def test_zero_delimeter():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_negative_delimeter():
    assert intersperse([1, 2, 3], -4) == [1, -4, 2, -4, 3]