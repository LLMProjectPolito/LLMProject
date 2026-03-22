import pytest

def test_compare_empty_lists():
    assert compare([], []) == []

def test_compare_equal_lists():
    assert compare([1, 2, 3], [1, 2, 3]) == [0, 0, 0]

def test_compare_different_lists():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 5, 0, 0, 0, 4], [4, 1, 1, 0, 0, -2]) == [4, 4, 1, 0, 0, 6]

def test_compare_negative_numbers():
    assert compare([-1, -2, -3], [-1, -2, -3]) == [0, 0, 0]
    assert compare([-1, -2, -3], [1, 2, 3]) == [2, 4, 6]
    assert compare([1, 2, 3], [-1, -2, -3]) == [2, 4, 6]

def test_compare_mixed_positive_negative():
    assert compare([1, -2, 3], [-1, 2, 3]) == [2, 4, 0]

def test_compare_large_numbers():
    assert compare([1000, 2000, 3000], [1000, 2000, 3000]) == [0, 0, 0]
    assert compare([1000, 2000, 3000], [1001, 1999, 3001]) == [1, 1, 1]

def test_compare_zero_values():
    assert compare([0, 0, 0], [0, 0, 0]) == [0, 0, 0]
    assert compare([0, 0, 0], [1, 2, 3]) == [1, 2, 3]
    assert compare([1, 2, 3], [0, 0, 0]) == [1, 2, 3]

def test_compare_single_element_lists():
    assert compare([5], [5]) == [0]
    assert compare([5], [10]) == [5]

def test_compare_different_length_lists():
    with pytest.raises(ValueError):
        compare([1, 2], [1])
    with pytest.raises(ValueError):
        compare([1], [1, 2])